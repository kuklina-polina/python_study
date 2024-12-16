import tkinter as tk
from tkinter import filedialog, ttk, Frame
from db_connection import DBConn
from file_for_import import *
from read_write_data import *

class DatabaseUploaderApp:
    def __init__(self, master):
        self.master = master
        master.title("Загрузка данных о выполненных работах в БД")

        self.frame = Frame(master, padx=10, pady=10)
        self.frame.pack(expand=True)

        self.create_widgets()

    def create_widgets(self):
        # Окна подключение к БД
        username_label = tk.Label(self.frame, text="Имя пользователя:")
        username_label.grid(row=0, column=0, sticky='w')
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1, sticky='w')

        password_label = tk.Label(self.frame, text="Пароль:")
        password_label.grid(row=1, column=0, sticky='w')
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky='w')

        self.connect_button = tk.Button(self.frame, text="Подключиться", command=self.db_connect)
        self.connect_button.grid(row=2, column=1, sticky='w')

        # Выбор типа данных
        type_data_label = ttk.Label(self.frame, text="Выберите тип данных:")
        type_data_label.grid(row=4, column=0, sticky='w')

        self.type_data = tk.StringVar(value="аэрофотосъёмка")  # Значение по умолчанию
        self.types_data = {
            "afs": "аэрофотосъёмка",
            "orthophoto": "ортофотопланы",
            "lidar": "лазерное сканирование",
            "megafon": "мегафон",
            "digital_city_plan": "цифровые планы городов",
            "digital_map": "цифровые карты"
        }

        self.types_data_menu = ttk.Combobox(self.frame, textvariable=self.type_data, values=list(self.types_data.values()), state='disabled')
        self.types_data_menu.grid(row=4, column=1, sticky='w')
        self.types_data_menu.bind('<<ComboboxSelected>>', self.browse_file_type)

        # Выбор файла
        browse_button_label = ttk.Label(self.frame, text="Выберите файл:")
        browse_button_label.grid(row=6, column=0, sticky='w')
        self.browse_button = ttk.Button(self.frame, text="...", command=self.browse_file, state=tk.DISABLED)
        self.browse_button.grid(row=6, column=1, sticky='w')
        self.filepath = ""

        # Подготовка и загрузка данных
        self.prepare_button = tk.Button(self.frame, text="Подготовить данные", command=self.prepare_data, state=tk.DISABLED)
        self.prepare_button.grid(row=8, column=1, sticky='w')

        self.upload_button = tk.Button(self.frame, text="Загрузить в БД", command=self.upload_data, state=tk.DISABLED)
        self.upload_button.grid(row=10, column=1, sticky='w')

        # Пустые строки
        empty_row1 = tk.Label(self.frame)
        empty_row1.grid(row=3, column=0, sticky='w')
        empty_row2 = tk.Label(self.frame)
        empty_row2.grid(row=5, column=0, sticky='w')
        empty_row3 = tk.Label(self.frame)
        empty_row3.grid(row=7, column=0, sticky='w')
        empty_row4 = tk.Label(self.frame)
        empty_row4.grid(row=9, column=0, sticky='w')

        #Строка состояния
        self.statusbar = tk.Label(self.master, text= "Готов к работе", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def db_connect(self):
        user = self.username_entry.get()
        password = self.password_entry.get()

        if not user or not password:
            self.statusbar.config(text= "Пожалуйста, заполните все поля.")
            return

        self.db_connection = DBConn(user, password)
        self.statusbar.config(text="Успешное подключение")
        self.types_data_menu.config(state = 'normal')

    def browse_file_type(self, event):
        self.filetype = self.type_data.get()
        if self.filetype:
            self.browse_button.config(state=tk.NORMAL)
        self.statusbar.config(text="Выберите файл для загрузки")

    def browse_file(self):
        self.filepath = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=(("MaiInfo TAB", "*.TAB, *.tab"), ("Esri ShapeFile", "*.shp"), ("All files", "*.*"))
        )

        if self.filepath:
            match self.filetype:
                case "ортофотопланы":
                    self.data = OrthoForImport(self.filetype, self.filepath, self.db_connection)
                case "лазерное сканирование":
                    # self.data = OrthoForImport(self.filetype, self.filepath)
                    print("lidar")
                case _:
                    print("all")
        else:
            return
        if self.data:
            self.prepare_button.config(state=tk.NORMAL)
        self.statusbar.config(text="Файл готов к обработке")

    def prepare_data(self):
        self.data.data = self.data.preprocessing(self.data.data)
        self.statusbar.config(text= f"Подготовка данных")

        self.upload_button.config(state=tk.NORMAL) # Разрешаем кнопку "Загрузить в БД" после подготовки данных

    def upload_data(self):
        self.statusbar.config(text= f"Загрузка данных в БД ") # Заглушка
        write_ortho_to_db(self.data)

        self.statusbar.config(text=f"Данные внесены в БД")


