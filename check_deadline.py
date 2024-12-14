from datetime import datetime as dt

#получение сегодняшней даты
date_now = dt.now()
print(f"Текущая дата: {date_now.strftime("%d-%m-%Y")}")

#запрашиваем у пользователя дату и удаляем пробелы по краям
issue_date = input("Введите дату дедлайна в формате (день-месяц-год) ").strip()

try:
    #перобразование строки в дату и вычисление разницы между сегодняшней даты и даты дедлайна
    issue_date = dt.strptime(issue_date, "%d-%m-%Y")
    date_diff = issue_date.date() - date_now.date()

    #на основе полученной разницы в днях вычисляем склонение слова "день"
    if 11 <= abs(date_diff.days) <= 19:
        word = "дней"
    elif abs(date_diff.days) % 10 == 1:
        word = "день"
    elif 2 <= abs(date_diff.days) % 10 <= 4:
        word = "дня"
    else:
        word = "дней"

    #определяем разницу между дедлайном и на её основе выводим сообщение
    if date_diff.days > 0:
        print(f"До дедлайна осталось {date_diff.days} {word}.")
    elif date_diff.days == 0:
        print("Дедлайн сегодня")
    else:
        print(f"Внимание! Дедлайн истёк {abs(date_diff.days)} {word} назад.")
except:
    input("Неправильный формат даты, повторите попытку")