#usertime.py
import jsonhandler as jsh

from string import printable
import time
from table2ascii import table2ascii as t2a, PresetStyle

def mapuser(user, string):
        usermap = jsh.openjsonfile('usermapping.json')
        usermap[user] = string
        return f"Dir wurde erfolgreich ein Alias erstellt."

def userread(user):
        localreaddata = jsh.openjsonfile('usercache.json')
        user = user.lower()



        try:
                userdata = str(localreaddata[user])
        except:
                return "nicht vorhanden."
        else:
                if userdata == 'false':
                        return 'False'
                
                userdatalen = len(userdata)
                hour, minute = userdata[:userdatalen//2], userdata[userdatalen//2:]

                return (hour + ':' + minute)

def userreadall():
        localreadall = jsh.openjsonfile('usercache.json')

        keys = [k for k, v in localreadall.items() if v == "false"]

        finallist = []
        i = 0

        for x in keys:
                del localreadall[x]
        if not localreadall:
                return "-> Keine.\n\n\n Bitch."
        else:
                for attribute, value in localreadall.items():

                        string = str(value)
                        firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                        finallist.append([attribute, firstpart + ":" + secondpart])
                
                finallist = t2a(
                        header=["User", "Zeit"],
                        body=finallist,
                        style=PresetStyle.thin_compact)
                print(finallist)
                return finallist


def userwrite(user, time):
        if type(time) is str:
                time=time.lower()
        localuserwrite = jsh.openjsonfile('usercache.json')
        user = user.lower()
        localuserwrite[user] = time

        jsh.savefile(localuserwrite, 'usercache.json')

def userdelete(user):
        localuserdelete = jsh.openjsonfile('usercache.json')
        user = user.lower()

        try:
                del localuserdelete[user]
        except:
                return "Diesen User gibt es nicht."

        else:
                jsh.savefile(localuserdelete,'usercache.json')
                return "Der User wurde gelöscht."

def setuserconst(user):
        user = user.lower()
        data = jsh.openjsonfile('userconstants.json')
        data[user]= ""
        jsh.savefile(data, 'userconstants.json')

def deluserconst(user):
        localuserdelete = jsh.openjsonfile('userconstants.json')
        user = user.lower()

        try:
                del localuserdelete[user]
        except:
                return "Diesen User gibt es nicht."

        jsh.savefile(localuserdelete,'userconstants.json')

def userreset():
        userresetlist = []
        localuserconstants = jsh.openjsonfile('userconstants.json')
        data = jsh.openjsonfile('usercache.json')
        for k,v in data:
                for x,y in localuserconstants:
                        if k != x:
                                data[y] = "false"
        jsh.savefile(data, 'usercache.json')

# TESTING:

if __name__ == "__main__":
        sleep = 2
        userwrite("Joshie", 1340)
        print("Userwrite Joshie, 1340 DONE")
        time.sleep(sleep)
        userwrite("Moritz", 1350)
        print("Userwrite Joshie, 1350 DONE")
        time.sleep(sleep)
        userwrite("Joshie", "False")
        print("Userwrite Joshie, False DONE")
        time.sleep(sleep)
        print(userread("Joshie"))
        print("Userread Joshie DONE")
        time.sleep(sleep)
        print(userreadall())
        print("Userreadall DONE")
        time.sleep(sleep)
        print(userreadall())
        print("Userreadall DONE")
        time.sleep(sleep)
        userreset()
        print("Userreset DONE")
        time.sleep(sleep)
        userreadall()
        print("Userreadall DONE")