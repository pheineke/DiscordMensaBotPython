#usertime.py
import json

with open('usercache.json', 'r') as f:
        data = json.load(f)

def userread(user):
        return data[user]

def userwrite(user, time):
        user = user.lower()
        data[user] = time
        with open('usercache.json', 'w') as f:
                json.dump(data,f)

userwrite("Joshie", 1340)
userread("Joshie")