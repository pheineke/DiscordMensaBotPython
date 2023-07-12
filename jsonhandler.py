#jsonhandler.py
import json

def openjsonfile(jsonfile):
        with open(jsonfile, 'r') as f:
                data = json.load(f)
                return data
        
def savefile(datas, file):
        with open(file, 'w') as f:
                json.dump(datas,f)