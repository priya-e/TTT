while True:
    player1 = input('Choose O or X: ').upper()
    if player1 == 'X' or player1 == 'O':
        break
    else:
        print('Must choose either O or X')
        continue

if player1 == 'O':
    player2 = 'X'
else:
    player2 = 'O'

print('player1:', player1)
print('player2:', player2)

symbol = '$'
current_player = [player1]
game_matrix = [symbol] * 9


# print game_matrix nicely
def print_matrix(m):
    for i in range(0, 3):
        for j in range(0, 3):
            print(m[3 * i + j], end=' ')
        print('\n')


# Play function
def play(game_matrix, current_player):
    while True:
        cel = input('Enter your block: ')
        cell = int(cel)
        if cell not in range(len(game_matrix)):
            print('Sorry', current_player[0], 'Entered cell is out of range')

            continue
        elif game_matrix[cell] != symbol:
            print('Sorry', current_player[0], 'Cell is occupied! Try another one')
            continue
        else:
            game_matrix[cell] = current_player[0]
            print_matrix(game_matrix)
            break


# Game_over
def row_check_report(nums):
    for i in range(0, 3):
        val = None
        isRowSame = True
        for j in range(0, 3):
            if val is None:
                val = nums[3 * i + j]
                continue
            if val != nums[3 * i + j] or val == symbol:
                isRowSame = False
                break
        if isRowSame:
            return True, val
    return False


def col_check_report(nums):
    for i in range(0, 3):
        val = None
        is_col_same = True
        for j in range(0, 3):
            if val is None:
                val = nums[3 * j + i]
                continue
            if val != nums[3 * j + i] or val == symbol:
                is_col_same = False
                break
        if is_col_same:
            return True, val
    return False


def diagonal_check_report(nums):
    val = None
    is_dia_same = True
    is_dia_same1 = True
    j = 0
    for i in range(0, 3):
        j = i
        if val is None:
            val = nums[3 * i + j]
            continue
        if val != nums[3 * i + j] or val == symbol:
            is_dia_same = False
            break
    val = None
    a = list(range(3))
    b = list(range(2, -1, -1))
    for i, j in zip(a, b):
        if val is None:
            val = nums[3 * i + j]
            continue
        if val != nums[3 * i + j] or val == symbol:
            is_dia_same1 = False
            break
    if is_dia_same or is_dia_same1:
        return True
    return False


def is_tie(nums):
    if symbol in nums:
        return False
    else:
        print('No Winner')
        return True


def is_there_a_winner(matrix):
    winner_result = row_check_report(matrix)
    if winner_result:
        return True, 'row'
    winner_result = col_check_report(matrix)
    if winner_result:
        return True, 'column'
    winner_result = diagonal_check_report(matrix)
    if winner_result:
        return True, 'diagonal'


# Flip function
def flip():
    if current_player[0] == player1:
        current_player[0] = player2
        return
    else:
        current_player[0] = player1
        return


while True:
    play(game_matrix, current_player)
    result = is_there_a_winner(game_matrix)
    if result:
        print(current_player[0], "wins the game by", result[1])
        break
    if is_tie(game_matrix):
        break
    flip()
