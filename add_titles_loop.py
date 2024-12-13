titles = [] # список для заметок


while True:
    title = input("Введите заголовок (оставьте пустым или введите 'стоп' для завершения): ").strip()
    if title == "" or title.lower() == "стоп": # если вводится пустая строка или слово "стоп" цикл прервётся
        break
    if title not in titles:
        titles.append(title)
    else:
        print("Такая заметка уже имеется в списке")


print("Заголовки заметки:")
for title in titles:
    print(f"-{title}")
