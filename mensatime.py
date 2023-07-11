import re
import numpy as np
import usertime

def check(messagecontent):
    messagesplit = re.split(r'[.: ]', messagecontent)

    myxs = messagesplit[0]
    mensatime = messagesplit[1:]
    equal = messagesplit[2:]
    time = messagesplit[3:]

    '''
    userread 0
    userreadall 1
    userwrite 2 None/False
    userwrite 3 True
    baduserinput 4

    userwritehour (and minute=zero 5

    userwritehourminute 6

    var <-
    '''

    if myxs == 'my':
        if equal[0] == '=' and time:
            if time[0] == 'False':
                return [2, 'False']
            elif time[0] == 'True':
                return [3, 'True']
            else:
                try:
                    hour = int(time[0])
                except:
                    return [4]
                else:
                    if (0 <= hour <= 24):
                        try:
                            minute = int(time[1])
                        except:
                            return [5, hour*100, hour]
                        else:
                            if (0 <= minute <= 59):
                                if minute == 0:
                                    return [5, hour*100, hour]
                                else:
                                    return [6, hour*100+minute, hour, minute]
                            else:
                                return [4]
                    else:
                        return [4]

                    
        else:
            return [0]

    elif myxs == 'xs':
        return [1]
    

# TESTING:

if __name__ == "__main__":
        print(check("xs.mensatime"))


    

