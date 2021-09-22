import json
import io

commands = json.loads(open("commands.json", "r").read())

def listcommands():
    commandsList = ""
    i = 0

    sortedList = commands;
    sortedList.sort(lambda x,y: cmp(len(x["full"] + " " + x["args"].join(" ")), len(y["full"] + " " + y["args"].join(" "))))
    columnLen = len(sortedList[0]["full"] + " " + sortedList[0]["args"].join(" "))

    while i < len(commands):
        commandsList += createColumn(commands[i]["short"], 4) + " " + createColumn(commands[i]["full"] + " " + commands[i]["args"].join(" "), columnLen + 4) + " " + commands[i]["description"]
        i += 1

    return commandsList

def createColumn(value, spaces):
    returnValue = ""
    i = 0

    while i < len(spaces):
        if i < len(value):
            returnValue += value[i]
        else:
            returnValue += " "

        i += 1

    return returnValue