from datetime import datetime

print(str(datetime.now().strftime("%H:%M")).replace(":", "")[2:])