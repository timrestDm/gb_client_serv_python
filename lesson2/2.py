# 2.	Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# a.	Создать функцию write_order_to_json(), в которую передается 5 параметров —
# товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# b.	Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json


orders = [
    {"item": "phone",
     "quantity": 4,
     "price": 70000,
     "buyer": "Ivan",
     "date": "03.04.2019"
     },
    {"item": "laptop",
     "quantity": 3,
     "price": 20000,
     "buyer": "Petr",
     "date": "01.04.2019"
     },
    {"item": "notebook",
     "quantity": 1,
     "price": 100000,
     "buyer": "Pavel",
     "date": "05.04.2019"
     },
]

def write_order_to_json(order_data):
    with open('orders.json', 'r') as file:
        json_data = json.load(file)
    orders = json_data['orders']
    orders.append(order_data)

    with open('orders.json', 'w') as f:
        f.write(json.dumps(json_data,indent=4))


for order in orders:
    write_order_to_json(order)