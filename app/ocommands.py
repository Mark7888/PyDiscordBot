from reload import reload
from settings import setting
from pyhelp import pyhelp
from configparser import ConfigParser

def ocommand(message, sprefix, ownerID, consol_prefix, log_prefix, client):
	# open lang file
	sconfig = ConfigParser()
	sconfig.read('../servers/' + message.server.id + '/serverconfig.ini')
	serverlang = sconfig.get('Config', 'lang')
	langfile = open("../config/lang/" + serverlang + ".lang", "r")
	lang = langfile.read().split("\n")

	msg = ""
	if message.content.upper().startswith(sprefix + "RELOAD"):
		if message.author.id == ownerID:
			reload(message, consol_prefix, log_prefix)
	elif message.content.upper().startswith(sprefix + "PYSETTINGS"):
		if message.author.server_permissions.administrator:
			msg = (setting(message))
		else:
			msg = lang[8]
	elif message.content.upper().startswith(sprefix + "PYHELP"):
		msg = (pyhelp(message))

	elif message.content.upper().startswith(sprefix + "PYCLEAN"):
		if message.author.server_permissions.manage_messages:
			msg = "clean"
		else:
			msg = lang[8]

	else:
		msg = lang[9]


	return(msg)
