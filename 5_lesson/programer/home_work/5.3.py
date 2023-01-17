# Создайте программу для игры в ""Крестики-нолики"".

def map_game(one, two, three, four, five, six, seven, eight, nine):
    print(f'| {one} | {two} | {three} |')
    print(' -----------')
    print(f'| {four} | {five} | {six} |')
    print(' -----------')
    print(f'| {seven} | {eight} | {nine} |')


def move_player(turn):
    if turn == 0:
        move = int(input("Куда поставите крестик?"))
    else:
        move = int(input("Куда поставите нолик??"))
    return move

winner = 0
turn = 0
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9

while turn < 3:
    map_game(one, two, three, four, five, six, seven, eight, nine)
    move = move_player(turn)
    if turn == 0:
        if move == 1:
            if one == 'X' or one == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                one = 'X'
                turn += 1
        if move == 2:
            if two == 'X' or two == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                two = 'X'
                turn += 1
        if move == 3:
            if three == 'X' or three == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                three = 'X'
                turn += 1
        if move == 4:
            if four == 'X' or four == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                four = 'X'
                turn += 1
        if move == 5:
            if five == 'X' or five == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                five = 'X'
                turn += 1
        if move == 6:
            if six == 'X' or six == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                six = 'X'
                turn += 1
        if move == 7:
            if seven == 'X' or seven == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                seven = 'X'
                turn += 1
        if move == 8:
            if eight == 'X' or eight == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                eight = 'X'
                turn += 1
        if move == 9:
            if nine == 'X' or nine == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                nine = 'X'
                turn += 1
        if (one == two and two == three) or (
        four == five and five == six) or (
        seven == eight and eight == nine) or (
        one == four and four == seven) or (
        two == five and five == eight) or (
        three == six and six == nine) or (
        one == five and five == nine) or (
        three == five and five == seven):
            turn = 'X'
            break
    else:
        if move == 1:
            if one == 'X' or one == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                one = '0'
                turn -= 1
        if move == 2:
            if two == 'X' or two == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                two = '0'
                turn -= 1
        if move == 3:
            if three == 'X' or three == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                three = '0'
                turn -= 1
        if move == 4:
            if four == 'X' or four == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                four = '0'
                turn -= 1
        if move == 5:
            if five == 'X' or five == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                five = '0'
                turn -= 1
        if move == 6:
            if six == 'X' or six == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                six = '0'
                turn -= 1
        if move == 7:
            if seven == 'X' or seven == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                seven = '0'
                turn -= 1
        if move == 8:
            if eight == 'X' or eight == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                eight = '0'
                turn -= 1
        if move == 9:
            if nine == 'X' or nine == '0':
                print('Клетка занята, давай по новой')
                move = move_player(turn)
            else:
                nine = '0'
                turn -= 1
        if (one == two and two == three) or (
        four == five and five == six) or (
        seven == eight and eight == nine) or (
        one == four and four == seven) or (
        two == five and five == eight) or (
        three == six and six == nine) or (
        one == five and five == nine) or (
        three == five and five == seven):
            turn = "0"
            break

print(f'Победил {turn}')