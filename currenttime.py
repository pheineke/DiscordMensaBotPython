import jsonhandler
from usertime import userreset as userreset
from datetime import datetime
import time

while True:
    currenttime = str(datetime.now().strftime("%H:%M"))
    if currenttime == "18:10":
        userreset()
        time.sleep(30)

