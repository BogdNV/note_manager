statuses = ["выполнено", "в процессе", "отложено"]

# Текущий статус заметки
current_status = "в процессе"
print(f"Текущий статус заметки: \"{current_status}\"\n")

print("Выберите новый статус заметки:\n1. выполнено\n2. в процессе\n3. отложено")

while True:
    try:
        status = int(input("Выберите новый статус (укажите число): "))
        if status not in (1, 2, 3):
            print(f"Ошибка введите число от 1 до {len(statuses)}")
        elif statuses[status-1] == current_status:
            print("Статус не обновлён")
        else:
            print(f"Статус заметки успешно обновлён на: \"{statuses[status-1]}\"")
            current_status = statuses[status-1]
            break

    except:
        print("Это не число, повторите попытку")