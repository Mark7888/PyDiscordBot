from subprocess import call
def reload(message, consol_prefix):
	print(consol_prefix + "Reloading...")
	stat = open("../config/status.file", "w")
	stat.write("RESTART")
	stat.close()
	call(['python3', 'main.py'])
	exit()
