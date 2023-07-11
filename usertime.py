#usertime.py
import os
import json
import time

def openfile():
        with open('usercache.json', 'r') as f:
                data = json.load(f)
                return data

def savefile(datas):
        with open('usercache.json', 'w') as f:
                json.dump(datas,f)

def userread(user):
        localreaddata = openfile()
        user = user.lower()
        userdata = str(localreaddata[user])
        userdatalen = len(userdata)
        hour, minute = userdata[:userdatalen//2], userdata[userdatalen//2:]

        return (hour+minute)

def userreadall():
        localreadall = openfile()

        keys = [k for k, v in localreadall.items() if v == "False"]

        for x in keys:
                del localreadall[x]
        return localreadall


def userwrite(user, time):
        localuserwrite = openfile()
        user = user.lower()
        localuserwrite[user] = time

        savefile(localuserwrite)

def userdelete(user):
        localuserdelete = openfile()

        user = user.lower()

        try:
                del localuserdelete["joshie"]
        except:
                return "Diesen User gibt es nicht."

        savefile(localuserdelete)




# TESTING:

if __name__ == "__main__":
        userwrite("Joshie", 1340)
        time.sleep(5)
        userwrite("Moritz", 1350)
        time.sleep(5)
        userwrite("Joshie", "False")
        time.sleep(5)
        print(userread("Joshie"))
        time.sleep(5)
        print(userreadall())
        time.sleep(5)
        print(userreadall())