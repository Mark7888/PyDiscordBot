from configparser import ConfigParser
from os import makedirs, path
from re import match
def addcommand(message, lang):

    msg = ""
    splits = {"description" : lang[16],
    "rank" : '0'}
    linemsg = message.content[1:].split("\n")
    arg = linemsg[0].split("&")
    if len(arg) <= 1:
        msg = lang[2]
        return(msg)
    arg[0] = arg[0].split(" ")[1]

    # server config file
    msg = ""
    sconfig = ConfigParser()
    sconfig.read('../servers/' + str(message.guild.id) + '/serverconfig.ini')
    serverlimit = sconfig.get('Config', 'limit')

    # separate the command's arguments
    while len(arg) > 0:
        if arg[0].startswith("name"):
            if arg[0][4] == "=":
                splits['name'] = arg[0][5:]
                arg = arg[1:]
            else:
                msg = lang[12]
                return(msg)

        elif arg[0].startswith("description"):
            if arg[0][11] == "=":
                splits['description'] = arg[0][12:]
                arg = arg[1:]
            else:
                msg = lang[12]
                return(msg)

        elif arg[0].startswith("text"):
            if arg[0][4] == "=":
                splits['text'] = arg[0][5:]
                arg = arg[1:]
            else:
                msg = lang[12]
                return(msg)

        elif arg[0].startswith("rank"):
            if arg[0][4] == "=":
                splits['rank'] = arg[0][5:]
                arg = arg[1:]
            else:
                msg = lang[12]
                return(msg)

        else:
            arg = arg[1:]
    # check the command's arguments
    if "text" not in splits or "name" not in splits:
        msg = lang[13]
        return(msg)
    characters = ["/", "<", ">", "|", ":", '"', "*", "?"]
    for char in characters:
        if char in splits['name']:
            msg = lang[19]
            return(msg)
    if not match("^[A-Za-z0-9_-]*$", splits['name']):
        msg = lang[47]
        return(msg)
    # open command list file
    commandlist = open('../servers/' + str(message.guild.id) + '/command.list', "r", encoding='utf-8')
    commands = commandlist.read()
    list = commands.split("\n")
    commandlist2 = open('../config/commands.list', "r", encoding='utf-8')
    commands2 = commandlist2.read()
    list2 = commands2.split(" ")
    list2.append("reload")
    list2.append("pyprefix")

    # check command limit
    if len(list) > int(serverlimit):
        msg = lang[48]
        return(msg)

    #create command
    if splits['name'] not in list:
        if splits['name'] not in list2:
            if not path.exists('../servers/' + str(message.guild.id) + '/commands'):
                makedirs('../servers/' + str(message.guild.id) + '/commands')
            commandfile = open('../servers/' + str(message.guild.id) + '/commands/' + splits['name'] + ".command", "w", encoding='utf-8')
            commandfile.write(splits['description'] + '\n' + splits['text'] + '\n' + splits['rank'] + '\n')
            commandfile.close()
            commandlist = open('../servers/' + str(message.guild.id) + '/command.list', "w", encoding='utf-8')
            commandlist.write(commands + splits['name'] + '\n')
            commandlist.close()
            msg = lang[15]
        else:
            msg = lang[39]
    else:
        msg = lang[14]

    return(msg)
