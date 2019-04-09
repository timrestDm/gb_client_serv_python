import socket
import json
import time
from argparse import ArgumentParser
# import yaml
from yaml import load, Loader

from settings import (
    HOST, PORT, ENCODING_NAME, BUFFER_SIZE)


host = HOST or ''
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
        host = config.get('host') or ''
        port = config.get('port') or PORT
        encoding_name = config.get('encoding_name') or ENCODING_NAME
        buffer_size = config.get('buffer_size') or BUFFER_SIZE
if args.addr:
    host = args.addr or ''
    if args.port:
        port = args.port or 7777


# разбираем полученный ответ от клиента
def get_recieved_data(data):
    return json.loads(data.decode(encoding_name))


# создаем ответ-сообщение с кодом для клиента
def create_response_message(response_code, type, text):
    mess = {'response': response_code, 'time':int(time.time())}
    if type == 'alert':
        mess['alert'] = text
    elif type == 'error':
        mess['error'] = text
    return mess


# конвертим сообщение в json
def set_json_to_send(data):
    return (json.dumps(data)).encode(encoding_name)


try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    print(f'Server started with {host}:{port}')
    while True:
        client, client_address = sock.accept()
        print(f'Client from address {client_address} connected')
        data_recieved = client.recv(buffer_size) # получили данные от клиента
        data = get_recieved_data(data_recieved) # разбираем эти данные
        print(data)
        data_to_send = create_response_message(200, 'alert', 'User presence on server')
        client.send(set_json_to_send(data_to_send))
except KeyboardInterrupt:
    print('Server closed')
