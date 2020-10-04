import os
import json

def walkFile(file):
    dirList = []
    for root,dirs,files in os.walk(file):
        for d in dirs:
            dirList.append(d)

    return dirList

def getMetadata():
    processName_dict = {}
    processName_list = []
    dirList = walkFile("./Presences")
    for path in dirList:
        with open(f'./Presences/{path}/metadata.json', mode='r', encoding='u8') as jfile:
            jdata = json.load(jfile)
        processName = jdata["process"]
        processName_list.append(processName)
        processName_dict[processName] = path

    return processName_list, processName_dict

def getData(path):
    with open(f'./Presences/{path}/metadata.json', mode='r', encoding='u8') as jfile:
        jdata = json.load(jfile)

    clientId = jdata['presence']['clientId']
    state = jdata['presence']['state']
    details = jdata['presence']['details']
    large_image = jdata['presence']['large_image']
    large_text = jdata['presence']['large_text']
    small_image = jdata['presence']['small_image']
    small_text = jdata['presence']['small_text']

    return clientId, state, details, large_image, large_text, small_image, small_text
