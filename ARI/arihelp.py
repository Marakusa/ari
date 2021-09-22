import json
import io

commands = json.loads(open("/usr/lib/ari/commands.json", "r").read())

def listcommands(args):
    commandsList = ""
    i = 0

    sortedList = sorted(commands, key=lambda x: len(x["full"] + " " + " ".join(x["args"])))
    columnLen = len(sortedList[len(sortedList) - 1]["full"] + " " + " ".join(sortedList[len(sortedList) - 1]["args"]))

    while i < len(commands):
        commandsList += createColumn(commands[i]["short"], 4) + " " + createColumn(commands[i]["full"] + " " + " ".join(commands[i]["args"]), columnLen + 4) + " " + commands[i]["description"]
        commandsList += "\n"
        i += 1

    print(commandsList)

def createColumn(value, spaces):
    returnValue = ""
    i = 0

    while i < spaces:
        if i < len(value):
            returnValue += value[i]
        else:
            returnValue += " "

        i += 1

    return returnValue
