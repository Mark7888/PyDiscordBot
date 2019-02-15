from os import path
from configparser import ConfigParser
config = ConfigParser()
def configcheck(warn_prefix):
    if not path.exists('../config/config.ini'):
        file = open('../config/config.ini', "w")
        file.write("""\
        [BotConfig]
        Token = ""
        ownerID = ""
        default_prefix = "!"
        """)
        print(warn_prefix + "The Config file was created in the 'config' folder.")
        exit()
