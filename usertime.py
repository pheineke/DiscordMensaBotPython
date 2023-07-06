#usertime.py
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
        if data[user] == "0":
                minute = "00"
        return (hour+minute)

def userreadall():
        keys = data.keys()
        for key, value in data.items():
            return str(key) + " " + str(value)
        print(keys)
        print(data.keys())


def userwrite(user, time):
        user = user.lower()
        data[user] = time

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