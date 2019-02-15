from ocommands import ocommand
from configcheck import configcheck
from scommands import scommand
from log import log
from subprocess import call
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
    await client.change_presence(game=discord.Game(name='Type |pyhelp| for more information'))

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
    scl = open("../servers/" + message.server.id + "/command.list", "r+")
    scls = scl.read().split(" ")

    # create server files
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
    langfile = open("../config/lang/" + serverlang + ".lang", "r")
    lang = langfile.read().split("\n")

    # server prefix
    sconfig = ConfigParser()
    sconfig.read('../servers/' + message.server.id + '/serverconfig.ini')
    sprefix = sconfig.get('Config', 'prefix')
    # message
    if message.content.startswith(sprefix):
        msg = ""
        if """%""" in message.content:
            msg = lang[1]
            await client.send_message(message.channel, msg)
            return
        msgargs = message.content[1:].split(" ")
        if msgargs[0].upper() in commandlist:
            msg = ocommand(message, sprefix, ownerID, consol_prefix, log_prefix, client)
            if msg == "clean":
                def is_me(m):
                        return m.author == client.user
                deleted = await client.purge_from(message.channel, limit=50, check=is_me)
                msg = lang[10] + " " + str(len(deleted)) + " " + lang[11]
            if msg != "":
                await client.send_message(message.channel, msg)
            log(message, msg, log_prefix)

        elif msgargs[0].upper() in scls:
            msg = scommand(message, sprefix, log_prefix)
            if msg != "":
                await client.send_message(message.channel, msg)
            log(message, msg, log_prefix)
try:
    client.run(Token)
except:
    print(warn_prefix + "Something went wrong. Please check the Token in the config file!")
    print(Fore.RED + "Error:")
