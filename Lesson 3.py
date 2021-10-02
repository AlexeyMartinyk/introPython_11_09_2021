# from random import randint
# min_limit = 1
# max_limit = 100
# comp_value = randint(1, 10)
#
# cur_value = int(input(f"Угадай число от {min_limit} до {max_limit}:"))
# go_game = True
# while cur_value != comp_value:
#  Тернарный Оператор   case_word = "мeньше" if cur_value > comp_value else "Больше"
#     cur_value = int(input(f"Попробуй число {case_word}"))
#
#     # if cur_value > comp_value:
#     #     cur_value = int(input("Попробуй число меньше:"))
#     # else:
#     #     cur_value = int(input("Попробуй число больше:"))
#
# print("Victory!!!")

# value = input("Введи цело число")
# try:
#     value_int = int(value)
#     result = value_int * 10
#     print(result)
# except ValueError:
#     print("это не число!!!")


###################################################################
#Циклы for
# for  врем_перем in итер_обьект:
#     итерация

# my_str = "qwerty123 $#% ASD"

# for symbol in my_str:
#     if symbol.lower() in "eyioa":
#         print(symbol)


########################################################################
#Кортежи tuple и Списки list
# итерируемые объекты
# my_tuple = (1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"])
#
# my_list = [1, -10, "qwe", False, 3.14, (-2, 0), ["a", "z"]]

# print(my_tuple, type(my_tuple))
# print(my_list, type(my_list))
#
# index = 3
# print(my_tuple[index], my_list[index])
#
# print(len(my_tuple), len(my_list))


#срезы как у строк
# new_list = my_list[1:-1]
# print(new_list)

# for value in my_list:
#     if type(value) == int:
#         print(value)
#
#
# my_tuple = (1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"]) #  КАРТЕЖ НЕ ИЗМЕНЯЕМЫЙ ТИП
#
# my_list = [1, -10, "qwe", False, 3.14, (-2, 0), ["a", "z"]] #  СПИСОК ИЗМЕНЯЕМЫЙ ТИП ДАННЫХ
#
# # my_list[1] = 100
# #
# # print(my_list)
#
# #распаковка картежей и списков
#
# my_tuple = (1, 2, "qwe")
#
# val_int_1, val_int_2, _ = my_tuple
#
# print(val_int_1)

# my_tuple = (1, (-2, 0), ["a", "z"])
# my_list = [1, (-2, 0), ["a", "z"]]
# my_tuple[-1][0] = 100
# print(my_list)

# my_table = [[1, 2], [3, 4]]
# my_table[1][1] = 24
# print(my_table)

# my_tuple = (1, 2, 3)
# print(id(my_tuple))
# my_tuple = (100, *my_tuple[1:])
# print(id(my_tuple))

# list_1 = [1, 2]
# list_2 = [3, 4]
# new_list = [list_1.copy(), list_2[:]] # срез это всегда копия
# print(new_list)
#
# list_1[0] = 100
# list_2[0] = 300
# print(new_list, list_1)

# new_list = list("new_tuple")
# print(new_list)
# new_str = "$".join(new_list)
# print(new_str)

filename = "lesson3.py.txt"
# # filename = filename.replace(".txt", "")
# filename_parts = filename.split(".")
# filename = ".".join(filename_parts[:-1])

filename = filename.rsplit(".", 1)
filename = filename [0]

print(filename)