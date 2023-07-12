import jsonhandler
import usertime
from datetime import datetime
import time

while True:
    currenttime = str(datetime.now().strftime("%H:%M:%S"))
    if currenttime == "15:00:00":
        usertime.userreset()
        time.sleep(2)

