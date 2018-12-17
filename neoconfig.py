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

host = os.environ.get('NEOPY_PORT_8080_TCP_ADDR', '127.0.0.1')
port = os.environ.get('NEOVM_SERVICE_PORT', '8080')

# cmd = 'gunicorn -b %s:%d -w 2 -k gevent app:application' % (host, int(port))
#cmd = 'gunicorn -b %s:%d -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" test:app' % (host, int(port))
cmd = 'gunicorn -k flask_sockets.worker test:app'
sys.argv = shlex.split(cmd)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - - %(asctime)s %(message)s', datefmt='[%b %d %H:%M:%S]')
os.chdir(os.path.abspath(os.path.dirname(__file__)))
gunicorn.app.wsgiapp.run()



