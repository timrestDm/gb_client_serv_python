# 1.	Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
#  из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
# a.	Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
# названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# b.	Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;
# c.	Проверить работу программы через вызов функции write_to_csv().

import re, csv

headers = ["Изготовитель ОС", "Название ОС", "Код продукта", "Тип системы"]
file_names = ["info_1.txt", "info_2.txt", "info_3.txt"]


def get_data(file_name):
    data = []
    with open(file_name) as file:
        for el_str in file:
            for header in headers:
                if re.match(header, el_str):
                    data.append(el_str.split(":")[1].strip())
    return data


def write_to_csv():
    main_data = []
    main_data.append(headers)
    for file_name in file_names:
        main_data.append(get_data(file_name))
    with open('result1.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in main_data:
            f_n_writer.writerow(row)


write_to_csv()

with open('result1.csv') as f_n:
    print(f_n.read())
