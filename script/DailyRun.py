from pydoc import classname
import schedule
from datetime import datetime
import time
from generic import *

def job():
    print("Testing", datetime.now())

schedule.every().day.at("17:21").do(job)
#schedule.every(10).seconds.do(job)


while True:
    schedule.run_pending()
    print('check')
    print(__file__)
    time.sleep(1)

schedule.clear()