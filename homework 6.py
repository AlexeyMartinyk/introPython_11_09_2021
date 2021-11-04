
import os
os.chdir("HW_DOCS")

def domains_point_free(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip()[1:] for line in file.readlines()]
    except FileNotFoundError as error:
        return f"No file {error}"

print(f'1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов и возвращает их в виде списка строк (названия возвращать без точки).: {domains_point_free("domain.txt")}')

# 2 ############################

def surnames(filename):
    with open(filename, "r") as file:
        return [line.split("\t")[1] for line in file.readlines()]


print(f'2. Каждая строка файла содержит номер, фамилию, страну, некоторое число:{surnames("names.txt")}')

# 3 #############################

from datetime import datetime

def dates(filename):

    result = []
    with open(filename, "r") as file:
        for line in file.readlines():
            my_line = line.split(" - ")
            if len(my_line) > 1:
                date = my_line[0]
                day, month, year = date.split()
                my_date = datetime.strptime(f"{day[:-2]} {month} {year}", "%d %B %Y")
                result.append(
                    {
                        "date_original": date,
                        "date_modified": datetime.strftime(my_date, "%d/%m/%Y"),
                    }
                )
    return result


print(f'3. Функция, которая получает в виде параметра имя файла (authors.txt) и возвращает список словарей:{dates("authors.txt")}')