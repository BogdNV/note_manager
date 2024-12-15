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

#функция для запроса статуса у пользователя
def get_status():
    statuses = ["новая", "в процессе", "выполнено"]
    while True:
        try:
            n = int(input("Введите статус заметки (укажите число)\n1.новая\n2.в процессе\n3.выполнено\n").strip())
            if 1 <= n <= len(statuses) - 1:
                return statuses[n - 1]
            else:
                print("Вы ввели неверное число!")

        except:
            print(MESSAGE)