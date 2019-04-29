from configparser import ConfigParser
from os import path

def commandlist(message, sprefix, lang):
    
    # commandlist
    commands = open('../servers/' + message.server.id + '/command.list', "r")
    list = commands.read()
    commandlist = list.split("\n")
    # list text
    def clist():
        msg = """ ```css
""" + lang[18]
        # commands description
        for desc in commandlist:
            if path.exists('../servers/' + message.server.id + '/commands/' + desc + ".command"):
                cdes = open('../servers/' + message.server.id + '/commands/' + desc + '.command', "r", encoding='utf-8')
                cdes = cdes.read().split("\n")
                print("ok")
                msg += '\n' + """
- """ + sprefix + desc + """
  /* """ + cdes[0] + """ */"""
        msg += "\n" + """``` """
        return(msg)
    # commands
    if list == "\n" or list == "":

        msg = lang[17]

    else:
        msg = lang[18] + '\n' + list
        msg = clist()

    return(msg)
