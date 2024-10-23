from datetime import datetime

def logger(error_type, line, code, message):
    fd = open("errors.log", "at", encoding = "utf-8")
    error = f"{error_type}: {datetime.now().strftime("%Y-%m-%d-%H.%M.%S")}: {code}: {__file__}: {line}: {message}\n"
    fd.write(error)
    fd.close()

if __name__ == "__main__":
    logger("ERROR", 1, 1, "Запущен файл с функцией самостоятельно")