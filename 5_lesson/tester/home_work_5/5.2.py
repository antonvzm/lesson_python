# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def candy(name, sum):
    if sum > 28:
        number_candy = int(input(f"{name}, введи колличество конфет которые возьмешь, от 1 до 28:"))
        while number_candy < 1 or number_candy > 28:
            number_candy = int(input(f"{name}, тебе же сказали, от 1 до 28 :3 :"))
        return number_candy
    else:
        number_candy = 28 - sum
        return number_candy

def game_log(name, candy, sum, diff):
    print(f'{name} забрал {candy} конфет, теперь у него {sum}. Осталось {diff} конфет.')

def two_players_mode(name_player_first, name_player_second, coin):

    sum_candy_first = 0
    sum_candy_second = 0
    candy_sum = 2021
    temp = 0

    if coin == 0:
        while candy_sum > 28: 
            number_candy = candy(name_player_first, candy_sum)
            candy_sum -= number_candy
            sum_candy_first += number_candy
            game_log(name_player_first, number_candy, sum_candy_first, candy_sum)
            if candy_sum <= 28:
                temp = 1
                break
            number_candy = candy(name_player_second, candy_sum)
            candy_sum -= number_candy
            sum_candy_second += number_candy
            game_log(name_player_second, number_candy, sum_candy_second, candy_sum)
            if candy_sum <= 28:
                temp = 0
                break

    else:
        while candy_sum > 28:

            number_candy = candy(name_player_second, candy_sum)
            candy_sum -= number_candy
            sum_candy_second += number_candy
            game_log(name_player_second, number_candy, sum_candy_second, candy_sum)
            if candy_sum <= 28:
                temp = 0
                break
            number_candy = candy(name_player_first, candy_sum)
            candy_sum -= number_candy
            sum_candy_first += number_candy
            game_log(name_player_first, number_candy, sum_candy_first, candy_sum)
            if candy_sum <= 28:
                temp = 1
                break
    return temp

def coin_toss(name_player_first, name_player_second):
    coin = randint(0,2)
    if coin == 0:
        print(f'Первым ходит {name_player_first}')
    else:
        print(f'Первым ходит {name_player_second}')
    return coin

def one_players_mode(name_player_first, name_player_second, coin):

    sum_candy_first = 0
    sum_candy_second = 0
    candy_sum = 2021
    temp = 0

    if coin == 0:
        while candy_sum > 28: 
            number_candy = candy(name_player_first, candy_sum)
            candy_sum -= number_candy
            sum_candy_first += number_candy
            game_log(name_player_first, number_candy, sum_candy_first, candy_sum)
            if candy_sum <= 28:
                temp = 1
                break
            number_candy = randint(1,29)
            candy_sum -= number_candy
            sum_candy_second += number_candy
            game_log(name_player_second, number_candy, sum_candy_second, candy_sum)
            if candy_sum <= 28:
                temp = 0
                break

    else:
        while candy_sum > 28:

            number_candy = randint(1,29)
            candy_sum -= number_candy
            sum_candy_second += number_candy
            game_log(name_player_second, number_candy, sum_candy_second, candy_sum)
            if candy_sum <= 28:
                temp = 0
                break
            number_candy = candy(name_player_first, candy_sum)
            candy_sum -= number_candy
            sum_candy_first += number_candy
            game_log(name_player_first, number_candy, sum_candy_first, candy_sum)
            if candy_sum <= 28:
                temp = 1
                break
    return temp

def battle_bot_mode(name_player_first, name_player_second, coin):

    sum_candy_first = 0
    sum_candy_second = 0
    candy_sum = 2021
    temp = 0

    if coin == 0:
        while candy_sum > 28: 
            number_candy = randint(1,29)
            candy_sum -= number_candy
            sum_candy_first += number_candy
            game_log(name_player_first, number_candy, sum_candy_first, candy_sum)
            if candy_sum <= 28:
                temp = 1
                break
            number_candy = randint(1,29)
            candy_sum -= number_candy
            sum_candy_second += number_candy
            game_log(name_player_second, number_candy, sum_candy_second, candy_sum)
            if candy_sum <= 28:
                temp = 0
                break

    else:
        while candy_sum > 28:

            number_candy = randint(1,29)
            candy_sum -= number_candy
            sum_candy_second += number_candy
            game_log(name_player_second, number_candy, sum_candy_second, candy_sum)
            if candy_sum <= 28:
                temp = 0
                break
            number_candy = randint(1,29)
            candy_sum -= number_candy
            sum_candy_first += number_candy
            game_log(name_player_first, number_candy, sum_candy_first, candy_sum)
            if candy_sum <= 28:
                temp = 1
                break
    return temp


number_player = int(input('Введи колличество игроков (1 или 2): '))
while number_player >= 3:
    number_player = int(input('Я не расслышал, можешь повторить? '))

if number_player == 1:
    name_player_first = input("Как тебя зовут? ")
    name_player_second = 'Бэндер'
    print(f'Хорошо {name_player_first}, с тобой сыграет Бэндер')
    coin = coin_toss(name_player_first, name_player_second)
    winner = one_players_mode(name_player_first, name_player_second, coin)
    if winner == 0:
        print(f'Победил {name_player_first}, ты молодец!')
    else:
        print(f'Победил {name_player_second}! Не расстраевайся {name_player_first}, {name_player_second} все таки машина и был создан для этой игры')
elif number_player == 2:
    name_player_first = input("Как зовут первого игрока? ")
    name_player_second = input("Как зовут второго игрока? ")
    print(f'Удачной игры {name_player_first} и {name_player_second}!')
    coin = coin_toss(name_player_first, name_player_second)
    winner = two_players_mode(name_player_first, name_player_second, coin)
    if winner == 0:
        print(f'Победил {name_player_first}, ты молодец! Не расстраивайся {name_player_second}, мы же оба понимаем что ты поддавался:3')
    else:
        print(f'Победил {name_player_second}, ты молодец!Не расстраивайся {name_player_first}, мы же оба понимаем что ты поддавался:3')
else:
    name_player_first = 'R2D2'
    name_player_second = 'Бэндер'
    print('Смотреть как кто то играет не так интересно, но если ты настаиваешь:D')
    coin = coin_toss(name_player_first, name_player_second)
    winner = battle_bot_mode(name_player_first, name_player_second, coin)
    if winner == 0:
        print(f'Во време ожесточенной борьбы, победу одержал {name_player_first}!')
    else:
        print(f'Во време ожесточенной борьбы, победу одержал {name_player_second}!')