import user_interface as i

while True:
    operation = int(input('Введите 1 для добавления номера, 2 для поиска контакта или 3 для отсановки работы: '))
    if operation == 1:
        i.add_phone()
    elif operation == 2:
        i.serch_phone(input('Введите информацию о пользователе: '))
    elif operation == 3:
        break
    else:
        operation = int(input('Некоректный ввод, введите 1 для добавления или 2 для поиска контакта: '))