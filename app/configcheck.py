from configparser import ConfigParser
config = ConfigParser()
def configcheck(warn_prefix):
    try:
        open('../config/config.ini', "r").close()

    except:
        file = open('../config/config.ini', "w")
        config['BotConfig'] = {
            'Token': '""',
            'ownerID': '""',
            'default_prefix': '"!"'
        }
        config.write(file)
        print(warn_prefix + "The Config file was created in the 'config' folder.")
        exit()
