from configparser import ConfigParser

def commandlist(message):
    # open lang file
    sconfig = ConfigParser()
    sconfig.read('../servers/' + message.server.id + '/serverconfig.ini')
    serverlang = sconfig.get('Config', 'lang')
    langfile = open("../config/lang/" + serverlang + ".lang", "r")
    lang = langfile.read().split("\n")

    commands = open('../servers/' + message.server.id + '/command.list', "r")
    list = commands.read()
    print("-------\n" + list + "\n------")
    if list == "\n" or list == "":
        msg = lang[17]
    else:
        msg = lang[18] + '\n' + list

    return(msg)
