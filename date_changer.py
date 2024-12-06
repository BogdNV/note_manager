from datetime import datetime as dt

created_date = input("Введите дату создания заметки в формате 'день-месяц-год' :").strip()
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год' :").strip()


temp_created_date = dt.strptime(created_date,"%d-%m-%Y").strftime("%d-%B")
temp_issue_date = dt.strptime(issue_date,"%d-%m-%Y").strftime("%d-%B")

print(temp_created_date, temp_issue_date, sep='\n')