# base from https://github.com/ninedraft/python-udp

import socket
import time
# Run Only for BroadcastINg
import json
from os import environ
from multiprocessing.connection import Listener
# from gpiozero import LineSensor
# sensor = LineSensor(4)

print('Start R.O.B.I.N. - STATUS BROADCASTER')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# address = ('localhost', 6000)
# listener = Listener(address)
# conn = listener.accept()

# Enable broadcasting mode
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)
try:
    uuid = environ["UUID"]
except:
    uuid = "undefinedUUID"
seq = 0

while True:
    # if conn.recv() == "update":
    #     seq += 1
    message = {'uuid': uuid, 'isFire': 1, 'seq': seq}
    print('send',message)
    messageByte = json.dumps(message).encode('utf-8')
    server.sendto(messageByte, ("112.116.44.15", 28795))
    time.sleep(1)
