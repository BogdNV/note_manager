from datetime import datetime as dt

MESSAGE = "Неверный формат, повторите попытку"

#функция для запроса даты дедлайна
def get_date(format):
    while True:
        try:
            date_string = input("Введите дедлайн (день-месяц-год): ").strip()
            date_string = dt.strptime(date_string, format).date()
            return date_string
        except:
            print(MESSAGE)