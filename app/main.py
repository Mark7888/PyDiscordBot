from ocommands import ocommand
from scommands import scommand
import datetime
from subprocess import call
from colorama import Fore, Back, Style
from colorama import init
import discord
from configparser import ConfigParser
init(autoreset=True)
client = discord.Client()
config = ConfigParser()
config.read('/config/config.ini')

# log
time = str(datetime.datetime.now())
time = time[:len(time)-7]
logtime = str(time[len(time)-8:])
log = open("/log/" + time + ".log", "w")

# read the config file
Token = config.get('BotConfig', 'Token')
ownerID = config.get('BotConfig', 'ownerID')
prefix = config.get('BotConfig', 'prefix')
Token = Token[1:len(Token)-1]
ownerID = ownerID[1:len(ownerID)-1]
adminID = "531927224840880141"
prefix = prefix[1:len(prefix)-1]

# set cmd prefixes
log_prefix = Fore.MAGENTA + "log - " + Fore.RESET
consol_prefix = Fore.YELLOW + Back.RED + Style.BRIGHT + "console" + Back.RESET + " - " + Style.RESET_ALL
server_prefix = Fore.GREEN + "[Server]: " + Fore.RESET

# read the command's list
commandfile = open("/config/commands.list", "r+")
commandlist = commandfile.read().split(" ")

# open status file
try:
    stat = open("/config/status.file", "r+")
except:
    stat = open("/config/status.file", "w").close()
    stat = open("/config/status.file", "r+")

# It runs if the bot is ready
@client.event
async def on_ready():
    if stat.read() == "RESTART":
        print(consol_prefix + "Reload completed.")
        stat.close()
        open("/config/status.file", "w").close()
    else:
        print('\n' + Fore.GREEN + "Logged in as:")
        print(Fore.CYAN + client.user.name + " <" + client.user.id + ">")
        print(Fore.GREEN + "---------------------------")
        print('\n' + Fore.RESET)
        stat.close()

# It runs if the bot get a message
@client.event
async def on_message(message):
    # we don't want the bot to reply to itself
    if message.author == client.user:
        return
    try:
        scl = open("/servers/" + message.server.id + "command.list", "r+")
    except:
        open("/servers/" + message.server.id + "command.list", "w").close()
        scl = open("/servers/" + message.server.id + "command.list", "r+")

    if message.content.startswith(prefix):
        msgargs = message.content[1:].split(" ")
        #if msgargs[0] in commandlist:
            #ocommand(message, msgargs, prefix, ownerID, adminID, consol_prefix)
        #elif msgargs[0] in scl:
            #scommand(message, msgargs, prefix, adminID)

client.run(Token)
