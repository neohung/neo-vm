#!/usr/bin/env python
import os
import json
import request
import gevent
import redis
from gevent.queue import Queue
from flask import Flask, render_template, send_from_directory, request
from flask_sockets import Sockets
from datetime import datetime, timedelta


REDIS_URL="redis://127.0.0.1:6379/0"
if 'REDIS_URL' in os.environ:
  REDIS_URL = os.environ['REDIS_URL']

app = Flask(__name__)
sockets = Sockets(app)
redis_server = redis.from_url(REDIS_URL)

class BackEndProcess(object):
    def __init__(self):
        self.receivers = list()
    def register(self,data):
        print("register client")
        self.receivers.append(data)
    def run(self):
        while True:
            now = (datetime.now()+timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "POST"
    elif request.method == 'GET':
        #return render_template('index.html')
        now = (datetime.now()+timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        return now+": TEST NEO"

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@sockets.route('/echo')
def receive(ws):
    bep.register(ws)
    while not ws.closed:
        message = ws.receive()
        print("receiver say: %s" % (message))
        ws.send("server got: "+message[::-1])
        gevent.sleep(0.1)

bep=BackEndProcess()
bep.start()
    
