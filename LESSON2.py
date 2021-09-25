temp = -12

# if temp > 0:
#     print("Можно шапку не надевать") если да!
# else:
#     print("надень шапку") Блок если нет!

# if temp > 0:
#     print("Можно шапку не надевать")
#     print("temp:", temp)
# else:
#     print("надень шапку")
#     print("End of else")


# from random import  randint
#
# case = randint(1, 6)
# print("выпало число:", case)
# if case == 6:
#     print("win Vasya!")
# elif case == 1:
#     print("win Petya!")
# else:
#     print("losser")

# if case > 3:
#     result = case **2
# else:
#     result = -case
# print("выпало число:", case, "result:", result)
###########################################################################
#тернарный оператор
# if case > 3:
#     result = case **2
# else:
#     result = -case

# result = case ** 2 if case > 3 else - case
# print("выпало число:", case, "result:", result)


##############################################################
# Строки и методы строк
# Форматирование строк

# case = 1
# result = "qwe"
# print(f"выпало число:{case}  с результатом:{result}")
#
#
# dirname = "home"
# filename = "test.py"
# path = f"{dirname}/{filename}"
# print(path)
# Литералы строк

# my_str_1 = "I'm Qwerty"
# my_str_2 = '"Apple" Inc.'
# my_str_3 = '''fsafafs'''
# my_str_4 = """I'm "Apple" Inc."""

#index = -1  последний с конца строки и так далеее.....



# index = 0
# symbol = my_str_1[index]
# # print(symbol)
# my_str_1_len = len(my_str_1)
# print(my_str_1_len, my_str_1[my_str_1_len - 1])

#срез строки
# new_str = my_str_1[1:5] # часть строки от левого индекса (включительно) до правого индекса ( не включительно)

# Замена символа на конерктном месте
# index = 5
# new_str = my_str_1[: index] + "K" + my_str_1[index + 1:]
# print(new_str)

# new_str = my_str_1[1:-1:2] #  каждый 2 символ, 2 - шаг среза
# new_str = my_str_1[::2] # символы на четных местах в строке
# new_str = my_str_1[1::2] # срез на нечетных местах
# new_str = my_str_1[::-1] # Зеркально отображение строки
# print(new_str)


my_str_1 = "I'm Qwerty"
#
# if my_str_1[-1] == "a":
#     print(f"a on last position in {my_str_1}")
# else:
#     print(f"a not on last position in {my_str_1}")
#
# for symbol in my_str_1: # строка итерируемый обьект
#     if symbol.lower() not in "eyuioa"  and symbol.isupper():
#         print(symbol)

# for symbol in my_str_1:
    # print(f"symbol'{symbol}' --> {ord(symbol)}")
for index in range(32, ord ('z') + 1):
    print(f"index: {index} --> '{chr(index)}'")

