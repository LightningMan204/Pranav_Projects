# If you want to know the time in any other notations:
# Just take cmd prompt or terminal and python3 <Your clock.py dir>
import datetime as dt

def Time():
    time = dt.datetime.now().strftime("%H:%M:%S")
    print(time)

Time()

def date():
    todaydate = dt.date.today()
    print(todaydate)

date()