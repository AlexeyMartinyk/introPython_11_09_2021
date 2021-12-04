import random, json
import os
import requests
from bs4 import BeautifulSoup
def restart_param():
    with open('sys.json', 'w') as sys_file:
        defolt = json.dump({"price": open_file_config()['price'], "valet": open_file_config()['valet'],
                            "usd_valet": open_file_config()['usd_valet']}, sys_file)
        return defolt
def open_file_config():
    with open('config.json', 'r') as config_file:
        data = json.load(config_file)
    return data
def write_file_sys():
    if os.stat("sys.json").st_size == 0:
        return
    else:
        with open('sys.json', 'w') as sys_file:
            json.dump({"price": price, "valet": valet, "usd_valet": usd_valet}, sys_file)
    return write_file_sys
def read_file_sys():
    with open('sys.json', 'r') as sys_file:
        write_file = json.load(sys_file)
    return write_file
def next_param():
    url = 'https://minfin.com.ua/currency/nbu/'
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text)
    table = soup.find('table', {'class': 'table-auto'})
    tr = table.find('td', {'class': 'responsive-hide'})
    tr_1 = tr.text
    tr_2 = tr_1[1:5]
    return float(tr_2)
def buy_param():
    global valet, usd_valet, price
    if os.stat("sys.json").st_size == 0:
        print("Enter RESTART")
    elif read_file_sys()['valet'] <= 0:
        price = read_file_sys()['price']
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        print("You do not have UAH to buy")
    elif read_file_sys()['valet'] > 0:
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        price = read_file_sys()['price']
        usd = float(input("Enter how many dollars you want to buy: "))
        usd_buy = usd * read_file_sys()['price']
        if read_file_sys()['valet'] - int(usd_buy) < 0:
            print("You don't have enough UAH", "\nYour wallet:", read_file_sys()['valet'], "ГРН\n"
                                                 "Course:", read_file_sys()['price'],"USD/UAH")
        else:
            valet = read_file_sys()['valet'] - usd_buy
            usd_valet = read_file_sys()['usd_valet'] + float(usd)
            price = read_file_sys()['price']
def buy_uah_param():
    global valet, usd_valet, price
    if os.stat("sys.json").st_size == 0:
        print("Enter RESTART")
    elif read_file_sys()['usd_valet'] <= 0:
        price = read_file_sys()['price']
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        print("You have no Dollars to sell")
    elif read_file_sys()['usd_valet'] > 0:
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        price = read_file_sys()['price']
        usd = float(input("Enter how much you want to buy UAH: "))
        usd_buy = usd / read_file_sys()['price']
        if read_file_sys()['usd_valet'] - int(usd_buy) < 0:
            print("You have no Dollars to sell", "\nYou wallet:", read_file_sys()['usd_valet'], "ГРН\n"
                                                 "Course:", read_file_sys()['price'],"USD/UAH")
        else:
            usd_valet= read_file_sys()['usd_valet'] - round(usd_buy,2)
            valet = read_file_sys()['valet'] + float(usd)
            price = read_file_sys()['price']
def buy_all_param():
    global valet, usd_valet, price
    if os.stat("sys.json").st_size == 0:
        print("Enter RESTART")
    elif read_file_sys()['valet'] <= 0:
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        price = read_file_sys()['price']
        print("You have no UAH to sell")
    else:
        price = read_file_sys()['price']
        usd = read_file_sys()['valet']/read_file_sys()['price'] # покупка доллара на все
        valet = read_file_sys()['valet'] - read_file_sys()['valet'] # перезапись грн кошелька
        usd_valet = round(read_file_sys()['usd_valet'] + usd, 2) # перезапись долл. кошелька
        print("USD:", usd_valet, "UAH:", valet)
def available_param():
    print("USD:", read_file_sys()['usd_valet'], "UAH:", read_file_sys()['valet'])
def sell_all_param():
    global valet, usd_valet, price
    if os.stat("sys.json").st_size == 0:
        print("Enter RESTART")
    elif read_file_sys()['usd_valet'] <= 0:
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        price = read_file_sys()['price']
        print("You have no Dollars to sell")
    else:
        price = read_file_sys()['price']
        buy_uah = read_file_sys()['usd_valet']*read_file_sys()['price']
        usd_valet = read_file_sys()['usd_valet'] - read_file_sys()['usd_valet']
        valet = round(read_file_sys()['valet'] + buy_uah, 2)
        print("USD:", usd_valet, "UAH:", valet)
def info_param():
    print("RESTART - Restart program;\nNEXT - update course;\nRATE - view course;\nBUY - buy USD;\n"
              "BUY_ALL - buy all usd;\nSELL_ALL - sell all usd;\nAVAILABLE - balance withdrawal;\n"
             "BUY_UAH - buy UAH;\nINFO - view command.")