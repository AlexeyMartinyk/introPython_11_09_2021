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


from random import  randint

case = randint(1, 6)
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

result = case ** 2 if case > 3 else - case
print("выпало число:", case, "result:", result)