# 1########################################################
# from collections import defaultdict
#
# persons = [{"name": "John", "age": 27}, {"name": "Johny", "age": 45},
#            {"name": "Martinuk", "age": 24}, {"name": "Yan", "age": 16},
#            {"name": "Oleksii", "age": 25}, {"name": "Jack", "age": 19}]
#
# age_by_names = defaultdict(list)
# len_name_by_names = defaultdict(list)
# ages = []
#
# for person in persons:
#     name = person["name"]
#     age = person["age"]
#     age_by_names[age].append(name)
#     len_name_by_names[len(name)].append(name)
#     ages.append(age)
#
# min_age = min(age_by_names)
# print('min_age:', *age_by_names[min_age])
#
# max_len_name = max(len_name_by_names)
# print('max_len_name:', *len_name_by_names[max_len_name])
#
# print('average:', sum(ages) // len(ages))

#2##################################################################################
# my_dict_1 = {
#     'unique_key_1': 'unique_value_1',
#     'key_1': 'value_1',
#     'key_2': 'value_2',
#     'unique_key_2': 'unique_value_2',
#     'unique_key_3': 'unique_value_3',
# }
#
# my_dict_2 = {
#     'unique_key_4': 'unique_value_4',
#     'key_1': 'value_3',
#     'key_2': 'value_2',
#     'unique_key_5': 'unique_value_5',
#     'unique_key_6': 'unique_value_6',
# }
#
# my_dict_1_keys = [key_1 for key_1 in my_dict_1.keys()]
# my_dict_2_keys = [key_2 for key_2 in my_dict_2.keys()]
#
# # a)
# my_dict_1_keys_set = set(my_dict_1_keys)
# my_dict_2_keys_set = set(my_dict_2_keys)
# both_dicts_keys = list(my_dict_1_keys_set.intersection(my_dict_2_keys_set))
# print(f'а) Создать список из ключей, которые есть в обоих словарях: {", ".join(both_dicts_keys)}')
#
# # б)
# unique_first_dict_keys = list(my_dict_1_keys_set.difference(my_dict_2_keys_set))
# print(f'б) Создать список из ключей, которые есть в первом, но нет во втором словаре: {", ".join(unique_first_dict_keys)}')
#
# # в)
# new_dict = {}
# for unique_first_dict_key in unique_first_dict_keys:
#     new_dict[unique_first_dict_key] = my_dict_1[unique_first_dict_key]
# print(f'в) Создать новый словарь из пар "ключ:значение", для ключей, которые есть в первом, но нет во втором словаре: {new_dict}')
#
# # Г)
# res = dict()
# for item in my_dict_1.items():
#     if item[0] not in my_dict_2:
#         res[item[0]] = item[1]
#     else:
#         res[item[0]] = [item[1], my_dict_2[item[0]]]
# for item in my_dict_2.items():
#     if item[0] not in my_dict_1:
#         res[item[0]] = item[1]
#     else:
#         res[item[0]] = [item[1], my_dict_1[item[0]]]
# print(f'г) Объединить эти два словаря в новый : {res}')
#3#########################################################
# my_list = ["qwe", "asd", "zxc", "qaz", "xsw", "edc"]
#
# def new_list(my_list):
#     result = []
#     for index in range(len(my_list)):
#         if not index % 2:
#             result.append(my_list[index][::-1])
#         else:
#             result.append(my_list[index])
#     return result
#
# print(new_list(my_list))

#
# 4###################################################################
# import random
# import string
# 
# names = ["John", "Pieter", "Sam", "Jim"]
# domains = ["com", "org", "net", "ua"]
# 
# def new_email(names, domains):
#     return str(random.choice(names)) + '.' + str(random.randint(100, 999)) + '@' + str(''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 7)))) + '.' + str(random.choice(domains))
# email = str(new_email(names, domains))
# print('4)', email)
