# AppLication For Read Entered Data
# base from https://github.com/ninedraft/python-udp
import socket
import json
import time
import requests
from os import environ

PORT = 28795
print('Start A.L.F.R.E.D - MESSAGE LISTENER at :{}'.format(PORT))
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP


try:
    uuid = environ["UUID"]
except:
    uuid = "undefinedUUID"
# Enable broadcasting mode
client.bind(("", PORT))
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

member = dict()
entry = dict()

while True:
    data, addr = client.recvfrom(1024)
    message = json.loads(data)
    recvTime = time.time()

    recvId = message["uuid"]
    seq = message["seq"]

    print("[{}] received message from <{}> status <{}> on <{}>".format(
        uuid, message["uuid"], message["isFire"], time.asctime(time.localtime(recvTime))))

    if recvId not in member or member[recvId]["seq"] != seq:
        try:
            req = requests.get("http://{}:8000/get".format(addr[0]))
            member[recvId] = {"ip": addr,
                              "information": req.json(), "seq": seq}

            print("new entry uuid <{}> with address <{}>".format(recvId, addr))
        except:
            print("Fetch from other joker fail")

    entry[recvId] = message["isFire"]
    payload = dict()
    for k,v in entry.items():
        payload[k] = {}
        if k in member:
            payload[k] = {**member[k]}
        payload[k]["isFire"] = message["isFire"]
        try:
            requests.post("http://localhost:8000/setpolldata",data=json.dumps(payload))
        except Exception as e:
            print("Update joker **may be** fail")