import platform
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

# check os type
if platform.system() == "Windows":
    systemsname = "windows"
elif platform.system() == "Linux":
    systemsname = "linux"
else:
    print(warn_prefix + "The auto updater is not compatible with this operation system!")
    exit()

# remove in linux : "sudo rm -rf .git"
# delete old bot update folder
if path.exists("./BotUpdate"):
    if systemsname == "windows":
        system('rmdir /S /Q "{}"'.format("./BotUpdate"))
    elif systemsname == "linux":
        system('sudo rm -rf ./BotUpdate')
# clone repo
Repo.clone_from("https://github.com/Mark7888/PyDiscordBot", "./BotUpdate")

if systemsname == "windows":
    system('rmdir /S /Q "{}"'.format("./BotUpdate/.git"))
elif systemsname == "linux":
    system('sudo rm -rf ./BotUpdate/.git')

# check version
if path.exists("../app.version"):
    oldversionfile = open("./BotUpdate/app.version", "r")
    newversionfile = open("../app.version", "r")
    oldversion = oldversionfile.read()
    newversion = newversionfile.read()
    if oldversion == newversion:
        print(Fore.YELLOW + "You have already installed the newest version.")
        exit()

# delete files
if systemsname == "windows":
    if path.exists("../app"):
        system('rmdir /S /Q "{}"'.format("../app"))
    if path.exists("../update/update.py"):
        osremove("../update/update.py")
    if path.exists("../config/lang"):
        system('rmdir /S /Q "{}"'.format("../config/lang"))
    if path.exists("../config/commands.list"):
        osremove("../config/commands.list")
    if path.exists("../app.version"):
        osremove("../app.version")
elif systemsname == "linux":
    if path.exists("../app"):
        system('sudo rm -rf ../app')
    if path.exists("../update/update.py"):
        osremove("../update/update.py")
    if path.exists("../config/lang"):
        system('sudo rm -rf ../config/lang')
    if path.exists("../config/commands.list"):
        osremove("../config/commands.list")
    if path.exists("../app.version"):
        osremove("../app.version")

# copy new files
copyfile("./BotUpdate/app", "../app")
copy2("./BotUpdate/update/update.py", "../update/update.py")
copyfile("./BotUpdate/config/lang", "../config/lang")
copy2("./BotUpdate/config/commands.list", "../config")
copy2("./BotUpdate/app.version", "../app.version")

# delete bot update folder
if path.exists("./BotUpdate"):
    if systemsname == "windows":
        system('rmdir /S /Q "{}"'.format("./BotUpdate"))
    elif systemsname == "linux":
        system('sudo rm -rf ./BotUpdate')

print(Fore.GREEN + "Bot successfully updated.")
