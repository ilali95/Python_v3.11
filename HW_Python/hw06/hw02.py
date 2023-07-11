# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, 
# решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, 
# определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

def is_valid(board):
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                return False
    return True

def eight_queens():
    import random
    solutions = []
    while len(solutions) < 4:
        board = random.sample(range(8), 8)
        if is_valid(board):
            solutions.append(board)
    for solution in solutions:
        print(solution)

eight_queens()