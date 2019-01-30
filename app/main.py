import datetime
from subprocess import call
from colorama import Fore, Back, Style
from colorama import init
import discord
from configparser import ConfigParser
init(autoreset=True)
client = discord.Client()
config = ConfigParser()
config.read('../config/config.ini')

#log
time = str(datetime.datetime.now())
time = time[:len(time)-7]
logtime = str(time[len(time)-8:])
log = open("../log/" + time + ".log", "w")

#read the config file
Token = config.get('BotConfig', 'Token')
ownerID = config.get('BotConfig', 'ownerID')
prefix = config.get('BotConfig', 'prefix')
Token = Token[1:len(Token)-1]
ownerID = ownerID[1:len(ownerID)-1]
adminID = "531927224840880141"
prefix = prefix[1:len(prefix)-1]
