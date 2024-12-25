from Data import date_now


#выводит на экран список заметок
def display_notes(notes):
    if notes:
        print("Список заметок:")
        print("-"*20)
        for i, note in enumerate(notes):
            print(f"{i+1}. Имя: {note.get('username', "")}")
            ind = " "*len(f"{i+1}. ")
            print(ind + f"Заголовок: {note.get("title", "")}")
            print(ind + f"Описание: {note.get("content", "")}")
            print(ind + f"Статус: {note.get("status","")}")
            print(ind + f"Дата создания: {note.get("created_date", date_now).strftime("%d-%m-%Y")}")
            print(ind + f"Дедлайн: {note.get("issue_date", date_now).strftime("%d-%m-%Y")}")
            print("-"*20)
        return True
    else:
        print("-" * 20)
        print("Список заметок пуст.")
        print("-" * 20)
        return False