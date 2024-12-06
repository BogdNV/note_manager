created_date = input("Введите дату создания заметки в формате 'день-месяц-год' :").strip()
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год' :").strip()


temp_created_date = created_date[:-5]
temp_issue_date = issue_date[:-5]

print(temp_created_date, temp_issue_date, sep='\n')