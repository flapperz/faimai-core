# base from https://github.com/ninedraft/python-udp

import socket
import time
from gpiozero import LineSensor
# Run Only for BroadcastINg
import json
from os import environ

print('Start R.O.B.I.N. - STATUS BROADCASTER')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Enable broadcasting mode
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)
sensor = LineSensor(4)
uuid = environ["UUID"]


while True:
    message = {'uuid': uuid, 'isFire': sensor.value == 1}
    messageByte = json.dumps(message).encode('utf-8')
    server.sendto(messageByte, ("112.116.44.15", 28795))
    # print("message sent!")
    time.sleep(1)
