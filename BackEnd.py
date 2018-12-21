#!/usr/bin/env python
import gevent
from flask_sockets import Sockets
from datetime import datetime, timedelta

class BackEndProcess(object):
    def __init__(self):
        self.receivers = list()
    def register(self,data):
        print("register client")
        self.receivers.append(data)
    def run(self):
        while True:
            now = (datetime.utcnow()+timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
            message=now
            for client in self.receivers:
                gevent.spawn(self.send, client, message)
            gevent.sleep(1)
        pass
    def start(self):
        gevent.spawn(self.run)
        pass
    def send(self, ws, message):
        try:
            ws.send(message)
        except Exception:
            print("Can't send data, Try to remove receiver")
            self.receivers.remove(ws)

