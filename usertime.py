#usertime.py
import os
import json
import time

def openusermapping():
        with open('usermapping.json', 'r') as f:
                data = json.load(f)
                return data

def openusercache():
        with open('usercache.json', 'r') as f:
                data = json.load(f)
                return data

def savefile(datas):
        with open('usercache.json', 'w') as f:
                json.dump(datas,f)


def mapuser(user, string):
        usermap = openusermapping()
        usermap[user] = string
        return f"Dir wurde erfolgreich ein Alias erstellt."

def userread(user):
        localreaddata = openusercache()
        user = user.lower()



        try:
                userdata = str(localreaddata[user])
        except:
                return "nicht vorhanden."
        else:
                userdatalen = len(userdata)
                hour, minute = userdata[:userdatalen//2], userdata[userdatalen//2:]

                return (hour+minute)

def userreadall():
        localreadall = openusercache()

        keys = [k for k, v in localreadall.items() if v == "False"]

        for x in keys:
                del localreadall[x]
        if not localreadall:
                return "-> Keine.\n\n\n Bitch."
        else:
                return localreadall


def userwrite(user, time):
        localuserwrite = openusercache()
        user = user.lower()
        localuserwrite[user] = time

        savefile(localuserwrite)

def userdelete(user):
        localuserdelete = openusercache()

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