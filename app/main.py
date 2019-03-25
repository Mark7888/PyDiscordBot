from ocommands import ocommand
from reload import reload
from pyhelp import pyhelp
from configcheck import configcheck
from scommands import scommand
from log import log
from os import makedirs, path
from colorama import Fore, Back, Style
from colorama import init
import discord
from configparser import ConfigParser
init(autoreset=True)
client = discord.Client()

# set cmd prefixes
log_prefix = Fore.MAGENTA + "log - " + Fore.RESET
consol_prefix = Fore.YELLOW + Back.RED + Style.BRIGHT + "console" + Back.RESET + " - " + Style.RESET_ALL
warn_prefix = Fore.YELLOW + Back.RED + Style.BRIGHT + "WARN" + Style.RESET_ALL + " - "
server_prefix = Fore.GREEN + "[Server]: " + Fore.RESET

# check the config file
configcheck(warn_prefix)

# read the config file
config = ConfigParser()
config.read('../config/config.ini')

Token = config.get('BotConfig', 'Token')
ownerID = config.get('BotConfig', 'ownerID')
prefix = config.get('BotConfig', 'default_prefix')
Token = Token[1:len(Token)-1]
ownerID = ownerID[1:len(ownerID)-1]
prefix = prefix[1:len(prefix)-1]
# check the Token
if Token == "":
    print(warn_prefix + "Please check the config file in the 'config' folder!")
    exit()
# read the command's list
commandfile = open("../config/commands.list", "r+")
commandlist = commandfile.read().split(" ")

# open status file
if not path.exists("../config/status.file"):
    stat = open("../config/status.file", "w").close()
stat = open("../config/status.file", "r+")

# It runs if the bot is ready
@client.event
async def on_ready():
    if stat.read() == "RESTART":
        print(consol_prefix + "Reload completed.")
        stat.close()
        open("../config/status.file", "w").close()
    else:
        print('\n' + Fore.GREEN + "Logged in as:")
        print(Fore.CYAN + client.user.name + " <" + client.user.id + ">")
        print(Fore.GREEN + "---------------------------")
        print('\n' + Fore.RESET)
        stat.close()
    await client.change_presence(game=discord.Game(name='Type |' + prefix + 'pyhelp| for more information'))

# It runs if the bot get a message
@client.event
async def on_message(message):
    # we don't want the bot to reply to itself
    if message.author == client.user:
        return
    # checks is the message in private
    if message.channel.is_private:
        return

    # create server folder
    if not path.exists("../servers/" + message.server.id):
        makedirs("../servers/" + message.server.id)

    if not path.exists("../servers/" + message.server.id + "/command.list"):
        open("../servers/" + message.server.id + "/command.list", "w").close()
    scl = open("../servers/" + message.server.id + "/command.list", "r+", encoding='utf-8')
    scls = scl.read().split("\n")

    if not path.exists("../servers/" + message.server.id + "/serverconfig.ini"):
        serverconfig = open("../servers/" + message.server.id + "/serverconfig.ini", "w")
        serverconfig.write('''[Config]\nprefix = ''' + prefix + '''\nlang = EN''')
        serverconfig.close()
    sconfig = ConfigParser()
    sconfig.read("../servers/" + message.server.id + "/serverconfig.ini")
    scfile = open("../servers/" + message.server.id + "/serverconfig.ini", "w")
    sconfig.set('Config', 'servername', message.server.name)
    sconfig.write(scfile)
    scfile.close()

    # open lang file
    sconfig = ConfigParser()
    sconfig.read('../servers/' + message.server.id + '/serverconfig.ini')
    serverlang = sconfig.get('Config', 'lang')
    langfile = open("../config/lang/" + serverlang + ".lang", "r", encoding='utf-8')
    lang = langfile.read().split("\n")

    # server prefix
    sconfig = ConfigParser()
    sconfig.read('../servers/' + message.server.id + '/serverconfig.ini')
    sprefix = sconfig.get('Config', 'prefix')
    # message
    if message.content.startswith(sprefix) or message .content.startswith(prefix):
        # empty command
        if len(message.content) == 1:
            return
        msg = ""
        # % in command
        if """%""" in message.content:
            msg = lang[1]
            await client.send_message(message.channel, msg)
            return
        msgargs = message.content[1:].split(" ")

        # original commands
        skipcommand = ["reload", "pyprefix"]
        if message.content.startswith(sprefix) and msgargs[0] not in skipcommand:
            if msgargs[0] in commandlist:
                msg = ocommand(message, sprefix, prefix, consol_prefix, log_prefix)
                # clean command
                if msg == "clean":
                    def is_me(m):
                            return m.author == client.user
                    try:
                        deleted = await client.purge_from(message.channel, limit=50, check=is_me)
                        msg = lang[10] + " " + str(len(deleted)) + " " + lang[11]
                    except:
                        msg = lang[20]
                #send message + log
                if msg != "":
                    await client.send_message(message.channel, msg)
                    log(message, msg, log_prefix)
            # server commands
            elif msgargs[0] in scls:
                msg = scommand(message, sprefix)
                if msg != "":
                    await client.send_message(message.channel, msg)
                log(message, msg, log_prefix)

        # fix prefix commands
        elif message.content.startswith(prefix):
            if message.content.startswith(prefix + "reload"):
                if message.author.id == ownerID:
                    reload(message, consol_prefix, log_prefix)
            elif message.content.startswith(prefix + "pyhelp"):
                msg = pyhelp(message, sprefix, prefix)
            elif message.content.startswith(prefix + "pyprefix"):
                msg = lang[37] + sprefix
                #send message + log
            if msg != "":
                await client.send_message(message.channel, msg)
                log(message, msg, log_prefix)


try:
    client.run(Token)
except:
    print(warn_prefix + "Something went wrong. Please check the Token in the config file!")
    print(Fore.RED + "Error:")
