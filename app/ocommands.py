from settings import setting
from addcommand import addcommand
from commandlist import commandlist
from removecommand import remove
from setcommand import set
from pyhelp import pyhelp
from configparser import ConfigParser

def ocommand(message, sprefix, prefix, consol_prefix, log_prefix):
	# open lang file
	sconfig = ConfigParser()
	sconfig.read('../servers/' + message.server.id + '/serverconfig.ini')
	serverlang = sconfig.get('Config', 'lang')
	langfile = open("../config/lang/" + serverlang + ".lang", "r", encoding='utf-8')
	lang = langfile.read().split("\n")

	msg = ""

	if message.content.startswith(sprefix + "pysettings"):
		if message.author.server_permissions.administrator:
			msg = (setting(message))
		else:
			msg = lang[8]
	elif message.content.startswith(sprefix + "pyhelp"):
		msg = pyhelp(message, sprefix, prefix)

	elif message.content.startswith(sprefix + "pycommandlist"):
		msg = (commandlist(message, sprefix))

	elif message.content.startswith(sprefix + "pyclean"):
		if message.author.server_permissions.manage_messages:
			msg = "clean"
		else:
			msg = lang[8]

	elif message.content.startswith(sprefix + "pyaddcommand"):
		if message.author.server_permissions.administrator:
			msg = (addcommand(message))
		else:
			msg = lang[8]

	elif message.content.startswith(sprefix + "pyremovecommand"):
		if message.author.server_permissions.administrator:
			msg = remove(message)
		else:
			msg = lang[8]

	elif message.content.startswith(sprefix + "pysetcommand"):
		if message.author.server_permissions.administrator:
			msg = set(message)
		else:
			msg = lang[8]

	else:
		msg = lang[9]


	return(msg)
