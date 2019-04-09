import socket
import json
import time
from argparse import ArgumentParser
from yaml import load, Loader

import settings
from settings import (
    HOST, PORT, ENCODING_NAME, BUFFER_SIZE
)

# ENCODING_NAME = 'utf-8'
# HOST = 'localhost'
# PORT = 8000
# BUFFER_SIZE = 1024

host = HOST or 'localhost'
port = PORT or 7777
encoding_name = ENCODING_NAME or 'utf-8'
buffer_size = BUFFER_SIZE or 1024

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration'
)

parser.add_argument(
    '-a', '--addr', type=str,
    help='Sets ip address of server'
)
parser.add_argument(
    '-p', '--port', type=str,
    help='Sets port of address of server'
)

args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        config = load(file, Loader=Loader)
        host = config.get('host') or HOST
        port = config.get('port') or PORT
        encoding_name = config.get('encoding_name') or ENCODING_NAME
        buffer_size = config.get('buffer_size') or BUFFER_SIZE
elif args.addr:
    host = args.addr or 'localhost'
    if args.port:
        port = args.port or 7777


# создаем presence сообщение для сервера
def create_presence_message(user_name, status, type):
    mess = {'action': 'presence', 'time':int(time.time())}
    if type:
        mess['type'] = type
    mess['user'] = {'account_name': user_name, 'status': status}
    return mess


# конвертим сообщение в json
def set_json_to_send(data):
    return (json.dumps(data)).encode(encoding_name)


# разбираем полученный ответ от сервера
def get_recieved_data(data):
    return json.loads(data.decode(encoding_name))


try:
    sock = socket.socket()
    sock.connect((host, port))
    print(f'Client started with {host}:{port}')
    while True:
        # value = input('Enter data to send:')
        # bvalue = value.encode(encoding_name)

        data_to_send = create_presence_message('tim', 'I am here', 'status') # создаем сообщение для отправки
        json_to_send = set_json_to_send(data_to_send) # конвертируем сообщение в json
        sock.send(json_to_send) # отправляем сообщение на сервер

        data_recieved = sock.recv(buffer_size)
        data = get_recieved_data(data_recieved)
        print(data['response'])
except KeyboardInterrupt:
    sock.close()
    print('Client closed')