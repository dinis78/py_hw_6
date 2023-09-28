# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам
# дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

#Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
# случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и
# выведите 4 успешных расстановки.

import random

def is_safe(board, row, col):
    # проверка по вертикали
    for i in range(row):
        if board[i] == col:
            return False
        
    # проверка главной доганали
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # проверка побочной диоганали
    i = row - 1
    j = col + 1
    while i >= 0 and j < 8:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    return True

def queens():
    board = [-1] * 8
    for row in range(8):
        col = random.randint(0, 7)
        while not is_safe(board, row, col):
            col = random.randint(0, 7)
        board[row] = col
    return board

def main():
    coutn = 0
    while coutn < 4:
        board = queens()
        if is_safe(board, 7, board[7]):
            print('Хорошая расстановка ферзей: ', board)
            coutn += 1

if __name__ == '__main__':
    main()













