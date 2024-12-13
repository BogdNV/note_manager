status = ["выполнено", "в процессе", "отложено"]
format_str = 'Текущий статус заметки: "{}"'

print(format_str.format(status[1]))
number_status = input("Выберите новый статус заметки:\n1. выполнено\n2. в процессе\n3. отложено\n").strip()

if not number_status.isdigit():
    print("не число")
else:
    number_status = int(number_status)
    print(f'Статус заметки успешно обновлён на: "{status[number_status-1]}"')