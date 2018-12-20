#!/usr/bin/env python
import os
import json
import gevent
import redis
from gevent.queue import Queue
from flask import Flask, render_template, send_from_directory, request
from flask_sockets import Sockets
from datetime import datetime, timedelta
import time
import random

REDIS_URL="redis://127.0.0.1:6379/0"
redis_server = redis.from_url(REDIS_URL)
for key in redis_server.scan_iter("testdata:*"):
  print(key)

TESTKEY="testdata:testlist"

now = (datetime.utcnow()+timedelta(hours=8))
timestamp = time.mktime(now.timetuple())
now_str = now.strftime("%Y-%m-%d %H:%M:%S")

data={"timestamp": timestamp, "data": random.random()}
jsondata = json.dumps(data)
redis_server.rpush(TESTKEY, jsondata)

for key in redis_server.scan_iter(TESTKEY):
    for i in range(0, redis_server.llen(TESTKEY)):
        tmpdata = redis_server.lindex(TESTKEY, i)
        jsontmpdata = json.loads(tmpdata)
        t = jsontmpdata.get('timestamp')
        val = jsontmpdata.get('data')
        print("%s:%f"%(datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S"),val))
