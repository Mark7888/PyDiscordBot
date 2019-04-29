from configparser import ConfigParser
from os import remove as removefile
from os import path
#if path.exists("<file_name>.txt"):
#   removefile("<file_name>.txt")

def remove(message, lang):
    msg = ""
    splits = {}
    arg = message.content[1:].split("&")
    arg[0] = arg[0].split(" ")[1]
    # separate the command's arguments
    while len(arg) > 0:
        if arg[0].startswith("name"):
            if arg[0][4] == "=":
                splits['name'] = arg[0][5:]
                arg = arg[1:]
            else:
                msg = lang[12]
                return(msg)
        else:
            arg = arg[1:]

    # check the command's arguments
    if "name" not in splits:
        msg = lang[44]
        return(msg)
    # open command list file
    commandlist = open('../servers/' + message.server.id + '/command.list', "r", encoding='utf-8')
    commands = commandlist.read()
    list = commands.split("\n")
    if splits['name'] not in list:
        msg = lang[45]
        return(msg)
    newlist = ""
    while len(list) > 1:
        if list[0] == splits['name']:
            list = list[1:]
        else:
            newlist = newlist + list[0] + "\n"
            list = list[1:]
    # remove in the commandlist file
    commandlist = open('../servers/' + message.server.id + '/command.list', "w", encoding='utf-8')
    commandlist.write(newlist)
    commandlist.close()
    # remove command file
    if path.exists('../servers/' + message.server.id + '/commands/' + splits['name'] + '.command'):
       removefile('../servers/' + message.server.id + '/commands/' + splits['name'] + '.command')
    msg = lang[46]
    return(msg)
