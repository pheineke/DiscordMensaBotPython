import re
import usertime

def check(messagecontent):
    messagesplit = re.split(r'[.: ]', messagecontent)

    myxs = messagesplit[0]
    mensatime = messagesplit[1:]
    equal = messagesplit[2:]
    time = messagesplit[3:]
    
    #return myxs, mensatime, equal, time


    '''
    userread 0
    userreadall 1
    userwrite 2 None/False
    userwrite 3 True

    userasconst 4 const/nconst

    userdelete 5

    baduserinput 5

    userwritehour (and minute=zero 6

    userwritehourminute 7


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
                else:
                    try:
                        hour = int(time0)
                    except:
                        return [6]
                    else:
                        if (0 <= hour <= 24):
                            try:
                                minute = int(time[1])
                            except:
                                return [7, hour*100, hour]
                            else:
                                if (0 <= minute <= 59):
                                    if minute == 0:
                                        return [7, hour*100, hour]
                                    else:
                                        return [8, hour*100+minute, hour, minute]
                                else:
                                    return [6]
                        else:
                            return [6]
            else:
                return[6]
             
        else:
            return [0]

    elif myxs == 'xs':
        return [1]
    

# TESTING:

# Array Eingaben mal anhand von length checken

if __name__ == "__main__":
        print(check("my.mensatime = none"))


    

