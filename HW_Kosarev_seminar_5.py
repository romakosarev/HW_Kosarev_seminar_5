# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# print(list(filter(lambda x: 'абв' not in x,input('введите текст: ').split())))



# 2. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

# import random
# name1 = input('введите имя первого игрока: ')
# name2 = input('введите имя второго игрока: ')
# hod = random.randrange(1,3)
# a = 2021
#
# if hod == 1:
#     print('Первый ход за ', name1)
# else:
#     print('Первый ход за ', name2)
#
# while a > 0:
#     if a > 28:
#         score1 = int(input('Ты можешь взять до 28 конфет за раз, сколько возьмешь?: '))
#         a = a - score1
#         if a > 28:
#             score2 = int(input('Ты можешь взять до 28 конфет за раз, сколько возьмешь?: '))
#             a = a - score2
#             if a <= 28:
#                 if hod ==1:
#                     print('Осталось ', a, 'конфет, их забирает ', name1, 'и побеждает в этой игре')
#                 else:
#                     print('Осталось ', a, 'конфет, их забирает ', name2, 'и побеждает в этой игре')
#         else:
#             if hod == 1:
#                 print('Осталось ', a, 'конфет, их забирает ', name1, 'и побеждает в этой игре')
#             else:
#                 print('Осталось ', a, 'конфет, их забирает ', name2, 'и побеждает в этой игре')





# 3. крестики нолики сам не осилил, скатал с интернета и разобрал, но метод не понравился, буду ждать разбора на уроке.

# board = list(range(1,10))
#
# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)
#
# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")
#
# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)
#
# input("Нажмите Enter для выхода!")



# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#
# with open('RLE.txt', 'r') as data:
#     my_text = data.read()
#
#
# def encode_rle(ss):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in ss:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code
#
#
# str_code = encode_rle(my_text)
# print(str_code)
# dev_12 = str_code
#
# with open('RLE_enc.txt', 'w') as data:
#     data.write(dev_12)