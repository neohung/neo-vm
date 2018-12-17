#!/usr/bin/env python
# coding:utf-8

import sys
import os
import logging
import shlex
import gunicorn.app.wsgiapp

workers = int(os.environ.get('GUNICORN_PROCESSES', '2'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))
forwarded_allow_ips = '*' 
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

host = os.environ.get('OPENSHIFT_DIY_IP', '127.0.0.1')
port = os.environ.get('OPENSHIFT_DIY_PORT', '8080')

# cmd = 'gunicorn -b %s:%d -w 2 -k gevent app:application' % (host, int(port))
cmd = 'gunicorn -b %s:%d -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" test:app' % (host, int(port))
sys.argv = shlex.split(cmd)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - - %(asctime)s %(message)s', datefmt='[%b %d %H:%M:%S]')
os.chdir(os.path.abspath(os.path.dirname(__file__)))
gunicorn.app.wsgiapp.run()


'''import os
import time
from datetime import datetime, timedelta
from flask import Flask

REDIS_URL="redis://127.0.0.1:6379/0"
if 'REDIS_URL' in os.environ:
  REDIS_URL = os.environ['REDIS_URL']


application = Flask(__name__)
sockets = Sockets(app)
redis_server = redis.from_url(REDIS_URL)

@application.route("/")
def hello():
    now = (datetime.now()+timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    return now+": "

if __name__ == "__main__":
    application.run()
'''
