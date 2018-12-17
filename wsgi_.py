#!/usr/bin/env python
# coding:utf-8

import os
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

