from configparser import ConfigParser
config = ConfigParser()
def configcheck(warn_prefix):
    try:
        file = open('../config/config.ini', "r").close()
        config.read(file)
        if config.get('BotConfig', 'Token') or config.get('BotConfig', 'ownerID') == '""':
            print(warn_prefix + "Please check the config file in the 'config' folder!")

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
