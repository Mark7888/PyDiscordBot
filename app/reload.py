import platform
from subprocess import call
def reload(message, consol_prefix, log_prefix):
	print(log_prefix + "Message from " + message.author.name + " <" + message.author.id + "> ")
	print(log_prefix + "Message: " + "'" + message.content + "'")
	print(consol_prefix + "Reloading...")
	stat = open("../config/status.file", "w")
	stat.write("RESTART")
	stat.close()
	# check os type
	if platform.system() == "Windows":
    		call(['python', 'main.py'])
	elif platform.system() == "Linux":
    		call(['python3', 'main.py'])
	exit()
