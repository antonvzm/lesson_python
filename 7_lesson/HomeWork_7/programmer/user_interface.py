import codecs

def add_phone():
    new_phone = input('Введите имя: ')
    new_phone = new_phone + ' ' + input('Введите фамилию: ')
    new_phone = new_phone + ' ' + input('Введите номер: ')
    new_phone = new_phone + ' ' + input('Введите описание: ')
    with open('7_lesson\\HomeWork_7\\programmer\\Phone_Book.txt', 'a', encoding='utf-8') as f:
        f.write(f'{new_phone}' + '\n')
        f.close()


def serch_phone(word):
    inp = iter(codecs.open('7_lesson\\HomeWork_7\\programmer\\Phone_Book.txt', encoding='utf-8').readlines())
    for i in inp:
        if word in i:
            print(i)