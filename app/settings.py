from re import match
from os import path
from configparser import ConfigParser
def setting(message, lang):

    # server config file
    msg = ""
    sconfig = ConfigParser()
    sconfig.read('../servers/' + str(message.guild.id) + '/serverconfig.ini')

    # settings command
    msgargs = message.content[1:].split(" ")
    if len(msgargs) > 1:
        if msgargs[1] == "prefix":
            if len(msgargs) > 2:
                file = open('../servers/' + str(message.guild.id) + '/serverconfig.ini', 'w')
                newprefix = msgargs[2]
                sconfig.set('Config', 'prefix', newprefix)
                sconfig.write(file)
                file.close()
                msg = lang[0] + " " + newprefix
            else:
                msg = lang[2]
        elif msgargs[1] == "lang":
            if len(msgargs) > 2:
                if path.exists("../config/lang/" + msgargs[2] + ".lang"):
                    file = open('../servers/' + str(message.guild.id) + '/serverconfig.ini', 'w')
                    newlang = msgargs[2]
                    sconfig.set('Config', 'lang', newlang)
                    sconfig.write(file)
                    file.close()

                    serverlang = sconfig.get('Config', 'lang')
                    langfile = open("../config/lang/" + serverlang + ".lang", "r", encoding='utf-8')
                    lang = langfile.read().split("\n")

                    msg = lang[4] + " " + msgargs[2]
                else:
                    msg = lang[5] + ' "' + msgargs[2] + '" ' + lang[6]
            else:
                msg = lang[2]


        elif msgargs[1] == "developer":
            if len(msgargs) > 2:
                roleid = msgargs[2]
                if len(roleid) > 5:
                    roleid = roleid[3:len(roleid)-1]
                else:
                    msg = lang[49]
                    return(msg)
                if match("^[0-9&-]*$", roleid):
                    file = open('../servers/' + str(message.guild.id) + '/serverconfig.ini', 'w')
                    sconfig.set('Config', 'devrole', roleid)
                    sconfig.write(file)
                    file.close()
                    msg = lang[50]
                else:
                    msg = lang[49]

            else:
                msg = lang[2]
        else:
            msg = lang[7]
    else:
        msg = lang[2]
    return(msg)
