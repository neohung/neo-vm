import os
import time
import datetime
from flask import Flask

REDIS_URL="redis://127.0.0.1:6379/0"
if 'REDIS_URL' in os.environ:
  REDIS_URL = os.environ['REDIS_URL']


application = Flask(__name__)

@application.route("/")
def hello():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return now+": "+REDIS_URL

if __name__ == "__main__":
    application.run()
