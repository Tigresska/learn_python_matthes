# Домашнее задание - проект 1: Крестики нолики
import random


# from IPython.display import clear_output
def display_board(av,board):
    """** Шаг 1: Напишите функцию, которая выводит на экран игровое поле.Поле можно
    хранить как список, где номера 1 - 9 соответствуют цифрам на цифровой клавиатуре.
    В итоге Вы получаете игровое поле 3 на 3. **"""
    # clear_output()
    print('\n' * 100)
    print(f'''
   |   |          |   |
 {av[7]} | {av[8]} | {av[9]}      {board[7]} | {board[8]} | {board[9]}
   |   |          |   |
-----------    -----------
   |   |          |   |
 {av[4]} | {av[5]} | {av[6]}      {board[4]} | {board[5]} | {board[6]}
   |   |          |   |
-----------    -----------
   |   |          |   |
 {av[1]} | {av[2]} | {av[3]}      {board[1]} | {board[2]} | {board[3]}
   |   |          |   |
    ''')


def player_input(name):
    '''** Шаг 2: Напишите функцию, которая спрашивает пользователя, какой символ он
    хочет использовать, 'X' или 'O'.Можно например использовать цикл * while * ,
    продолжая спрашивать до тех пор, пока пользователь не введёт корректный вариант ответа.**'''
    player = ''
    while player not in ('X', 'O'):
        player = input(
            f"Пожалуйста {name} выберите символ 'X' или 'O'").upper()
    return player


def place_marker(av,board, marker, position):
    '''** Шаг 3: Напишите функцию,
которая принимает на вход объект игровое поле(список),
символ('X' или 'O'), желаемую позицию(число 1 - 9), и помещает этот символ на игровое поле. **'''
    board[position] = marker
    av[position] = ' '


def win_check(board, mark):
    '''** Шаг 4: Напишите функцию, которая берёт игровое поле, символ(X или O) и
затем проверяет, выиграл ли этот символ. **'''
    if ((board[1] == board[2] == board[3] == mark)
            or (board[4] == board[5] == board[6] == mark)
            or (board[7] == board[8] == board[9] == mark)
            or (board[1] == board[4] == board[7] == mark)
            or (board[2] == board[5] == board[8] == mark)
            or (board[3] == board[6] == board[9] == mark)
            or (board[1] == board[5] == board[9] == mark)
            or (board[3] == board[5] == board[7] == mark)):
        return True
    else:
        return False


def choose_first():
    '''** Шаг 5: Напишите функцию, которая использует модуль random, чтобы случайным
образом решить, какой из игроков ходит первым.Можете например использовать
random.randint().Верните строку с информацией о том, кто из игроков ходит первым. **'''
    return random.randint(-1, 1)


def space_check(board, position):
    '''** Шаг 6: Напишите функцию, которая возвращает значение boolean в зависимости
от того, является ли указанное место на игровом поле пустым или нет. **'''
    return board[position] == ' '


def full_board_check(board):
    '''** Шаг 7: Напишите функцию, которая проверяет, является ли игровое поле полностью
заполненным, и возвращает значение boolean - True если полностью заполнено, иначе False. **'''
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board, player):
    '''** Шаг 8: Напишите функцию, которая запрашивает у игрока следующую позицию
(как число 1 - 9), и затем использует функцию с шага 6, чтобы проверить,
является ли эта позиция пустой.Если да, то возвращает эту позицию для дальнейшего использования. **'''
    while True:
        position = int(input(f'Пожалуйста {player} введите число'))
        if position >= 1 and position <= 9 and space_check(board, position):
            return position


def replay():
    '''** Шаг 9: Напишите функцию, которая спрашивает игрока, хочет ли он сыграть
снова, и возвращает True если игрок говорит "Yes"("да"). **'''
    answer = input('Хотите сыграть снова? ').lower()
    return answer in ('yes', 'да')


# ** Шаг 10: Это сложная часть! Используйте циклы while и созданные Вами
# функции, чтобы запустить игру! **


while True:
    print('Добро пожаловать в игру Крестики-Нолики!')
    # Настройка игры
    game_board = [' '] * 10
    available = list(str(i) for i in range(10))
    # display_board(game_board)

    togle = choose_first()
    players = ('#',
               {'name': 'Игрок 1', 'mark': ''},
               {'name': 'Игрок 2', 'mark': ''})

    print(f"Первым игроком стал {players[togle]['name']}!")
    players[togle]['mark'] = player_input(players[togle]['name'])
    if players[togle]['mark'] == 'X':
        players[togle * -1]['mark'] = 'O'
    else:
        players[togle * -1]['mark'] = 'X'

    play_game = input('Вы готовы играть? Введите Yes или No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:

            display_board(available,game_board)
            position = player_choice(game_board, players[togle]['name'])
            place_marker(available, game_board, players[togle]['mark'], position)
            display_board(available,game_board)
            if win_check(game_board, players[togle]['mark']):
                print(
                    f"Выиграл игрок {players[togle]['name']} игравший за {players[togle]['mark']}")
                game_on = False
            else:
                if full_board_check(game_board):
                    print('Ничья!!!')
                    break
                else:
                    togle *= -1
                    display_board(available,game_board)
    if not replay():
        break

#
##Хорошая работа!
