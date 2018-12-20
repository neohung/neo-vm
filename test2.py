import os
import json
import gevent
import redis
from gevent.queue import Queue
from flask import Flask, render_template, send_from_directory, request, redirect, flash, url_for
from flask_sockets import Sockets
from datetime import datetime, timedelta

app = Flask(__name__, template_folder='static/template')
app.config['SECRET_KEY'] = os.urandom(24)

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
