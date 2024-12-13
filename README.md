

## Описание файлов

### 1. `greetings.py`
Содержит функционал для вывода приветственного сообщения пользователю, предоставляя начальную информацию о приложении.

### 2. `date_changer.py`
Реализует преобразование формата отображения дат для пользователя. Даты `created_date` и `issue_date` отображаются без года.

### 3. `add_input.py`
Позволяет пользователю вводить данные через консоль. Предусмотрены подсказки для правильного ввода данных, включая формат дат.

### 4. `add_list.py`
Добавляет возможность ввода трёх заголовков, которые сохраняются в список. Все введённые данные выводятся вместе с этим списком заголовков.

### 5. `final.py`
Собирает все данные в структуру словаря. Ключевые поля словаря: `username`, `title`, `content`, `status`, `created_date`, `issue_date`. Все данные выводятся на экран в структурированном формате.

### 6. `add_titles_loop.py`
Реализует интерактивное добавление заголовков заметок. 
Пользователь может вводить любое количество заголовков, завершив ввод специальной командой (например, "стоп" или пустой строкой). 
Все введённые заголовки собираются в список, который затем выводится на экран. Программа игнорирует вводы, которые уже есть в списке.

### 7. `update_status.py`
Программа отображает текущий статус заметки. 
Обеспечивается возможность изменить статус на один из предложенных вариантов.

---

## Примечание
Код разработан для учебных целей и демонстрирует основы работы с переменными, пользовательским вводом, списками и словарями в Python.