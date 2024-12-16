import tkinter as tk
from database_uploader import DatabaseUploaderApp


if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseUploaderApp(root)
    root.mainloop()