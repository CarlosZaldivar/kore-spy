from datetime import datetime
import json
import requests
from scapy.all import *

last_home_click = datetime.now()


def is_home_click(payload_dict):
    if payload_dict['method'] != 'GUI.ActivateWindow':
        return False

    if 'params' not in payload_dict:
        return False

    if 'window' not in payload_dict['params']:
        return False

    if payload_dict['params']['window'] != 'home':
        return False

    return True


def is_suspend(payload_dict):
    return payload_dict['method'] == 'System.Suspend'


def read(packet):
    global last_home_click
    try:
        payload = packet.getlayer(TCP).payload
        if type(payload) is scapy.packet.Raw:
            payload_dict = json.loads(bytes(payload).decode('utf-8'))

            if is_home_click(payload_dict):
                if (datetime.now() - last_home_click).total_seconds() < 1:
                    requests.post('http://localhost:5000/device/0/power', json={'state': 'on'})
                last_home_click = datetime.now()
            if is_suspend(payload_dict):
                requests.post('http://localhost:5000/device/0/power', json={'state': 'off'})

    except Exception as e:
        print(e)


sniff(prn=read, iface='eth0', filter="dst port 9090")
