def configcheck(warn_prefix):
    try:
        open('/config/config.ini', "r").close()
        config = ConfigParser()
        config.read('/config/config.ini')
        if config.get('BotConfig', 'Token') or config.get('BotConfig', 'ownerID') or config.get('BotConfig', 'default_prefix') == '""':
            print(warn_prefix + "Please check the config file in the 'config' folder!")

    except:
        file = open('/config/config.ini', "w")
        file.write('''[BotConfig]
        Token: ""
        ownerID: ""
        default_prefix: ""''')
        file.close()

        print(warn_prefix + "The Config file was created in the 'config' folder.")
