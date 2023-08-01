import jsonhandler
from usertime import userreset as userreset
from table2ascii import table2ascii as t2a, PresetStyle
from datetime import datetime
import time

while True:
    currenttime = str(datetime.now().strftime("%H:%M"))
    if currenttime == "15:00":
        userreset()
        time.sleep(2)

