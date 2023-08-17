import re
import usertime

def check(messagecontent):
    messagesplit = re.split(r'[.: ​]', messagecontent)

    myxs = messagesplit[0]
    mensatime = messagesplit[1:]
    equal = messagesplit[2:]
    time = messagesplit[3:]
    try:
        elselist = messagesplit[4:]
        elselistlen = len(elselist)
        
    except:
        print("Nothing else")
    
    print(myxs, mensatime, equal, time)


    '''
    userread 0
    userreadall 1
    userwrite 2 None/False
    userwrite 3 True

    userasconst 4 const/nconst

    userdelete 5

    baduserinput 6

    userwritehourminute 7

    usersetuser 8


    var <-
    '''

    if myxs == 'my':
        if '=' in messagecontent:
            if equal[0] == '=' and time:
                time0 = time[0].lower()
                if time0 == 'false' or time0 == 'none':
                    return [2, 'false']
                elif time0 == 'true':
                    return [3, 'true']
                elif time0 == 'constant' or time0 == 'const':
                    return [4, 'const']
                elif time0 == 'notconstant' or time0 == 'nconst':
                    return [4, 'nconst']
                elif time0 == 'del' or time0 == 'delete':
                    return [5]
                elif '<@' in time0 and '>' in time0:
                    return [8, time0]
                elif not elselist:
                    return [6]
                else:
                    try:
                        hour = int(time0)
                    except:
                        return [6]
                    else:
                        if hour == 0:
                            hourstr = "00"
                        elif 0 < hour < 10:
                            hourstr = "0" + str(hour)
                        elif 9 < hour < 24:
                            hourstr = str(hour)
                        
                        try:
                            minute = int(time[1])
                        except:
                            return [7, hourstr + "00", hourstr, "00"]
                        else:
                            if minute == 0:
                                minutestr = "00"
                            elif 0 < minute < 10:
                                minutestr = "0" + str(minute)
                            elif 9 < minute < 60:
                                minutestr = str(minute)

                            return [7, hourstr + minutestr, hourstr, minutestr]
                
            else:
                return[6]
             
        else:
            return [0]

    elif myxs == 'xs':
        return [1]
    

# TESTING:

# Array Eingaben mal anhand von length checken
# Variable Wochentage

if __name__ == "__main__":
        print(check("my.mensatime = none"))


    

