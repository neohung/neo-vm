#!/usr/bin/env python
import json
import gevent
from gevent.queue import Queue
from flask import Flask, render_template, send_from_directory
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)


@app.route('/')
def index():
    return render_template('index.html')
    return "TEST NEO"

