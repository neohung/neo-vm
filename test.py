#!/usr/bin/env python3
import os
import json
import gevent
import redis
from gevent.queue import Queue
from flask import Flask, render_template, send_from_directory, request, redirect, flash, url_for
from flask_sockets import Sockets
from datetime import datetime, timedelta


REDIS_URL="redis://127.0.0.1:6379/0"
#if 'REDIS_URL' in os.environ:
#  REDIS_URL = os.environ['REDIS_URL']

app = Flask(__name__, template_folder='static/template')
app.config['SECRET_KEY'] = os.urandom(24)

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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "POST"
    elif request.method == 'GET':
        data = {'btn':0,'y':0,'x':0,'dx':0,'dy':0,'keycode': 0}
        return render_template('index.html',
                   title='Home',
                   mouse_keyboard = data
               )
        #print("GET")
        #now = (datetime.now()+timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        #return now+": TEST NEO"

@app.route('/login', methods=['GET', 'POST'])
def login():
    flash('2You CANT logged in')
    flash('1You CANT logged in')
    #print(url_for('indexx'))
    return redirect(url_for('index'))
    

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@sockets.route('/echo')
def receive(ws):
    bep.register(ws)
    while not ws.closed:
        message = ws.receive()
        if (message == "cam"):
            print("receiver say: %s" % (message))
            ws.send("server got: "+message[::-1])
            p = redis_server.pubsub()
            p.subscribe("cam")
            message = p.get_message()
            print(message)
        if (message == "rsave"):
            print("rsave")
            redis_server.set('test', 'working')
        if (message == "rload"):
            print(redis_server.get('test'))
        gevent.sleep(0.1)

bep=BackEndProcess()
bep.start()

#if __name__ == "__main__":
#    from gevent import pywsgi
#    from geventwebsocket.handler import WebSocketHandler
#    server = pywsgi.WSGIServer(('', 8080), app, handler_class=WebSocketHandler)
#    server.serve_forever()
