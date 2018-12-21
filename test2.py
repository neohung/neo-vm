#!/usr/bin/env python
import os
import json
import gevent
import redis
from gevent.queue import Queue
from flask import Flask, render_template, send_from_directory, request, redirect, flash, url_for,jsonify
from flask_sockets import Sockets
from datetime import datetime, timedelta

from BackEnd import BackEndProcess

REDIS_URL="redis://127.0.0.1:6379/0"

app = Flask(__name__, template_folder='static/template')
app.config['SECRET_KEY'] = os.urandom(24)

sockets = Sockets(app)
#redis_server = redis.from_url(REDIS_URL)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("GOT POST")
        data = request.form["filecontent"]
        print("GOT POST END")
        return jsonify({'msg': 'success'})
    elif request.method == 'GET':
        data = {'btn':0,'y':0,'x':0,'dx':0,'dy':0,'keycode': 0}
        return render_template('index.html',
                   title='Home',
                   mouse_keyboard = data
               )

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
            #p = redis_server.pubsub()
            #p.subscribe("cam")
            #message = p.get_message()
            #print(message)
        if (message == "rsave"):
            print("rsave")
            #redis_server.set('test', 'working')
        if (message == "rload"):
            pass
            #print(redis_server.get('test'))
        gevent.sleep(0.1)

@app.route('/login', methods=['GET', 'POST'])
def login():
    flash('2You CANT logged in')
    flash('1You CANT logged in')
    #print(url_for('indexx'))
    return redirect(url_for('index'))


bep=BackEndProcess()
bep.start()

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 8080), app, handler_class=WebSocketHandler)
    server.serve_forever()

