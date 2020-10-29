# base from https://github.com/ninedraft/python-udp
import socket
import json
import time
from os import environ

print('Start receiver')
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP

client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

uuid = environ["UUID"]
# Enable broadcasting mode
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

member = dict()

client.bind(("", 37020))
while True:
    data, addr = client.recvfrom(1024)
    message = json.loads(data)
    recvTime = time.time()

    recvId = message["uuid"]

    if recvId != uuid: 
        print("[{}] received message from <{}> status <{}> on <{}>".format(uuid, message["uuid"], message["status"], time.asctime(time.localtime(recvTime))))
        
        if recvId not in member:
            member[recvId] = addr
            print("new entry uuid <{}> with address <{}>".format(recvId, addr))
