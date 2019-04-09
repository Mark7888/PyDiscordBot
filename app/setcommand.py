from configparser import ConfigParser

def set(message):
    msg = ""
    # open lang file
    sconfig = ConfigParser()
    sconfig.read('../servers/' + message.server.id + '/serverconfig.ini')
    serverlang = sconfig.get('Config', 'lang')
    langfile = open("../config/lang/" + serverlang + ".lang", "r", encoding='utf-8')
    lang = langfile.read().split("\n")
    splits = {}
    arg = message.content[1:].split("&")
    if len(arg) <= 1:
        msg = lang[2]
        return(msg)
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
    if "name" not in splits:
        msg = lang[43]
        return(msg)

    if "description" not in splits and "text" not in splits and "rank" not in splits:
        msg = lang[40]
        return(msg)

    # open command list file
    commandlist = open('../servers/' + message.server.id + '/command.list', "r", encoding='utf-8')
    commands = commandlist.read()
    list = commands.split("\n")
    if splits['name'] in list:
        commandfile = open('../servers/' + message.server.id + '/commands/' + splits['name'] + ".command", "r", encoding='utf-8')
        old = commandfile.read().split("\n")
        command = {"description" : old[0],
        "text" : old[1]}
        if len(old) > 2:
            command["rank"] = old[2]
        else:
            command["rank"] = '0'

        if "description" in splits:
            command['description'] = splits['description']
        if "text" in splits:
            command['text'] = splits['text']
        if "rank" in splits:
            command['rank'] = splits['rank']
        new = command['description'] + "\n" + command['text'] + "\n" + command['rank'] + "\n"
        commandfile = open('../servers/' + message.server.id + '/commands/' + splits['name'] + ".command", "w", encoding='utf-8')
        commandfile.write(new)
        commandfile.close()
        msg = lang[41]

    else:
        msg = lang[42]
    return(msg)
