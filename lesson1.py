#1. Каждое из слов «разработка», «сокет», «декоратор» представить в
# строковом формате и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в
# формат Unicode и также проверить тип и содержимое переменных.


dev = 'разработка'

socket = 'сокет'

decorator = 'декоратор'

print(f'Вывод слов - {dev}, {socket}, {decorator} ') # return Вывод слов - разработка, сокет, декоратор
print(f'Вывод типов - {type(dev)}, {type(socket)}, {type(decorator)} ') # return Вывод типов - <class 'str'>, <class 'str'>, <class 'str'>

# in Unicode

dev_u = '\u0440\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u043A\u0430' # = 'разработка'

print(f'Вывод слов - {dev_u}') # return Вывод слов - разработка
print(f'Вывод типов - {type(dev_u)}') # return Вывод типов - <class 'str'>


#2. Каждое из слов «class», «function», «method» записать в байтовом типе
# без преобразования в последовательность кодов (не используя методы encode и decode)
#  и определить тип, содержимое и длину соответствующих переменных.

cl = b'class'
func = b'function'
mthd = b'method'

print(f'Тип - {type(cl)}') # return Тип - <class 'bytes'>
print(f'Содержимое - {cl}') # return Содержимое - b'class'
print(f'Длина - {len(cl)}') # return Длина - 5


#3. Определить, какие из слов «attribute», «класс», «функция»,
#  «type» невозможно записать в байтовом типе.

a_1 = b'attribute'
#a_2 = b'класс' # return SyntaxError: bytes can only contain ASCII literal characters.
#a_3 = b'функция' # return SyntaxError: bytes can only contain ASCII literal characters.
a_4 = b'type'

print(f'Тип attribute - {type(a_1)}') # return Тип - <class 'bytes'>
#print(f'Типы класс- {type(a_2)}')
#print(f'Типы функция - {type(a_3)}')
print(f'Типы type - {type(a_4)}') # return Тип - <class 'bytes'>


#4. Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и
# выполнить обратное преобразование (используя методы encode и decode).

a_1 = 'разработка'
a_2 = 'администрирование'
a_3 = 'protocol'
a_4 = 'standard'

a_1_b  = a_1.encode('utf-8')
a_2_b  = a_2.encode('utf-8')
a_3_b  = a_3.encode('utf-8')
a_4_b  = a_4.encode('utf-8')

print(f'{a_1_b}, {a_2_b}, {a_3_b}, {a_4_b}')
# return b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
# b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5',
# b'protocol', b'standard'

a_1  = a_1_b.decode('utf-8')
a_2  = a_2_b.decode('utf-8')
a_3  = a_3_b.decode('utf-8')
a_4  = a_4_b.decode('utf-8')

print(f'{a_1}, {a_2}, {a_3}, {a_4}') # return разработка, администрирование, protocol, standard


# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess

args = ['ping', 'yandex.ru']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in subproc_ping.stdout:
    print(line.decode('cp866').encode('utf-8').decode('utf-8'))

#return
# Обмен пакетами с yandex.ru [5.255.255.70] с 32 байтами данных:

# Ответ от 5.255.255.70: число байт=32 время=129мс TTL=55
# Ответ от 5.255.255.70: число байт=32 время=11мс TTL=55
# Ответ от 5.255.255.70: число байт=32 время=10мс TTL=55
# Ответ от 5.255.255.70: число байт=32 время=6мс TTL=55
#
# Статистика Ping для 5.255.255.70:
# Пакетов: отправлено = 4, получено = 4, потеряно = 0
# (0% потерь)
# Приблизительное время приема-передачи в мс:
# Минимальное = 6мсек, Максимальное = 129 мсек, Среднее = 39 мсек


#6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
# «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

f_n = open("test_file.txt", "r")
f_n.close()
print(f_n) #return <_io.TextIOWrapper name='test_file.txt' mode='w' encoding='cp1251'> (encoding='cp1251')

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')
# return UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte
