from subprocess import call
import platform

def reload(message, consol_prefix, log_prefix):
	print(log_prefix + "Message from " + message.author.name + " <" + str(message.author.id) + "> ")
	print(log_prefix + "Message: " + "'" + message.content + "'")
	print(consol_prefix + "Reloading...")
	stat = open("../config/status.file", "w")
	stat.write("RESTART")
	stat.close()
	if platform.system() == "Windows":
	    call(['python', 'main.py'])
	else:
		call(['python3', 'main.py'])
	exit()
