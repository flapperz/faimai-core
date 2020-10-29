# base from https://github.com/ninedraft/python-udp

import socket
import time
import json
from os import environ

print('Start sender')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting mode
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)

uuid = environ["UUID"]

message = { 'uuid': uuid, 'status': 'nofire' }
messageByte = json.dumps(message).encode('utf-8')

while True:
    server.sendto(messageByte, ("<broadcast>", 37020))
    # print("message sent!")
    time.sleep(1)