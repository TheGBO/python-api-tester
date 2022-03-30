import datetime
import time

def current_time():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')
    return st

def current_date():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    return st

def logstr(string):
    print(string)
    with open(f"logs/{current_date()}.log", 'a+') as f:
        f.write(string+"\n")