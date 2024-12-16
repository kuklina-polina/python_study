import geopandas as gpd
from tkinter import ttk
import tkinter as tk


def get_all_label_texts(parent):
    texts = []
    for child in parent.winfo_children():
        if isinstance(child, tk.Label):
            texts.append(child.cget("text"))
    return texts

def get_all_entries(parent):
    entries = []
    for child in parent.winfo_children():
        if isinstance(child, tk.Entry):
            entries.append(child)
    return entrie


def create_entry_fields(values):
    """Создает поля ввода на основе входного списка и возвращает словарь значений."""

    param = {}
    window_preprocessing = tk.Toplevel()
    window_preprocessing.title("Введите значения")

    entries = {} # Словарь для хранения полей ввода

    for i, value in enumerate(values):
        label = ttk.Label(window_preprocessing, text=f"{value}:")
        label.grid(row=i, column=0, padx=5, pady=2, sticky="w")
        entry = ttk.Entry(window_preprocessing)
        entry.grid(row=i, column=1, padx=5, pady=2)
        entries[value] = entry # Сохраняем ссылку на поле ввода

    def result():
        try:
            for value, entry in entries.items():
                param[value] = entry.get()
            window_preprocessing.destroy()
        except Exception as e:
            print(f"Ошибка при обработке ввода: {e}")

    button = tk.Button(window_preprocessing, text="Выполнить", command=result)
    button.grid(row=len(values), column=1, sticky='w')

    window_preprocessing.protocol("WM_DELETE_WINDOW", lambda: window_preprocessing.destroy()) #Обработка закрытия окна без нажатия кнопки

    window_preprocessing.wait_window() # Ждем закрытия окна

    return param



def read_mapinfo_tab(filepath):
    '''Читает файл MapInfo TAB и возвращает GeoDataFrame.'''
    try:
        gdf = gpd.read_file(filepath)
        return gdf
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None


def write_ortho_to_db(data):
    '''Записывает GeoDataFrame в БД.'''
    data_to_import = data.data
    data_to_import.to_postgis('orthophoto', schema='orthophoto', con=data.conn.conn, if_exists='append', index=False)
