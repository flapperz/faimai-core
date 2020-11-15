# AppLication For Read Entered Data
# base from https://github.com/ninedraft/python-udp
import socket
import json
import time
import requests
import gpiozero
from os import environ

PORT = 28795
print('Start A.L.F.R.E.D - MESSAGE LISTENER at :{}'.format(PORT))
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP


uuid = environ["UUID"]
# Enable broadcasting mode
client.bind(("", PORT))
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

member = dict()

while True:
    data, addr = client.recvfrom(1024)
    message = json.loads(data)
    recvTime = time.time()

    recvId = message["uuid"]

    if recvId != uuid:
        print("[{}] received message from <{}> status <{}> on <{}>".format(
            uuid, message["uuid"], message["status"], time.asctime(time.localtime(recvTime))))

        if recvId not in member:
            print("call at {}".format("{}:8000".format(addr)))
            req = requests.get("{}:8000".format(addr))
            member[recvId] = {"ip": addr, "information": req.json()}
            print(member)
            print("new entry uuid <{}> with address <{}>".format(recvId, addr))
