from shutil import copytree as copyfile
from shutil import copy2
from os import system, path
from os import remove as osremove
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
# commandline prefix
warn_prefix = Fore.YELLOW + Back.RED + Style.BRIGHT + "WARN" + Style.RESET_ALL + " - "
# check git
try:
    from git import Repo
except:
    print(warn_prefix + "GitPython requires git being installed on the system, and accessible via system's PATH.")
    exit()
# delete old bot update folder
if path.exists("./BotUpdate"):
    system('rmdir /S /Q "{}"'.format("./BotUpdate"))
# clone repo
Repo.clone_from("https://github.com/Mark7888/PyDiscordBot", "./BotUpdate")
system('rmdir /S /Q "{}"'.format("./BotUpdate/.git"))
# check version
if path.exists("../app.version"):
    oldversionfile = open("./BotUpdate/app.version", "r")
    newversionfile = open("../app.version", "r")
    oldversion = oldversionfile.read()
    newversion = newversionfile.read()
    if oldversion == newversion:
        print("You have already installed the newest version.")
        exit()

# delete files
if path.exists("../app"):
    system('rmdir /S /Q "{}"'.format("../app"))
if path.exists("../update"):
    system('rmdir /S /Q "{}"'.format("../update"))
if path.exists("../config/lang"):
    system('rmdir /S /Q "{}"'.format("../config/lang"))
if path.exists("../config/commands.list"):
    osremove("../config/commands.list")
if path.exists("../app.version"):
    osremove("../app.version")

# copy new files
copyfile("./BotUpdate/app", "../app")
copyfile("./BotUpdate/update", "../update")
copyfile("./BotUpdate/config/lang", "../config/lang")
copy2("./BotUpdate/config/commands.list", "../config")
copy2("./BotUpdate/app.version", "../app.version")

# delete bot update folder
if path.exists("./BotUpdate"):
    system('rmdir /S /Q "{}"'.format("./BotUpdate"))
