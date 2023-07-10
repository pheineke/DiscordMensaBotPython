#usertime.py
import os
import json
import time


with open('usercache.json', 'r') as f:
                data = json.load(f)

def savefile():
        with open('usercache.json', 'w') as f:
                json.dump(data,f)

def userread(user):
        user = user.lower()
        userdata = str(data[user])
        userdatalen = len(userdata)
        hour, minute = userdata[:userdatalen//2], userdata[userdatalen//2:]
        if "0" in data[user]:
                minute = "00"

        return (hour+minute)

def userreadall():
        datalocal = data
        keys = [k for k, v in datalocal.items() if v is None]


        for x in keys:
                userdelete(x)
        local = json.dumps(datalocal, indent=4)
        return local


def userwrite(user, time=None, status=None):
        user = user.lower()
        timestatus = {}
        timestatus[time] = status
        '''
        if status is None:
                data[user][time] = ""
        elif status.lower() == "none":
                data[user][time] = "none"
        '''
        
        data[user] = timestatus

        savefile()

def userdelete(user):
        user = user.lower()

        if user in data:
                del data[user]
        else:
                raise Exception("user does not exist")    

        savefile()




# TESTING:

if __name__ == "__main__":
        userwrite("Joshie", 1340)
        time.sleep(5)
        userwrite("Moritz", 1350)
        time.sleep(5)
        print(userread("Joshie"))
        time.sleep(5)
        userdelete("Joshie")
        userreadall()