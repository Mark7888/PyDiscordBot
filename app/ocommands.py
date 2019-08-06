from settings import setting
from addcommand import addcommand
from commandlist import commandlist
from removecommand import remove
from setcommand import set
from pyhelp import pyhelp
from configparser import ConfigParser

def ocommand(message, sprefix, prefix, consol_prefix, log_prefix,  devrole, lang, ownerID):

	msg = ""

	permissions = message.channel.permissions_for(message.author)

	if message.content.startswith(sprefix + "pysettings"):
		if permissions.administrator or str(message.author.id) == ownerID:# or devrole in memberranks:
			msg = (setting(message, lang))
		else:
			msg = lang[8]
	elif message.content.startswith(sprefix + "pyhelp"):
		msg = pyhelp(message, sprefix, prefix, lang)

	elif message.content.startswith(sprefix + "pycommandlist"):
		msg = (commandlist(message, sprefix, lang))

	elif message.content.startswith(sprefix + "pyclean"):
		if permissions.manage_messages or str(message.author.id) == ownerID:# or devrole in memberranks:
			msg = "clean"
		else:
			msg = lang[8]

	elif message.content.startswith(sprefix + "pyaddcommand"):
		if permissions.administrator or str(message.author.id) == ownerID:# or devrole in memberranks:
			msg = (addcommand(message, lang))
		else:
			msg = lang[8]

	elif message.content.startswith(sprefix + "pyremovecommand"):
		if permissions.administrator or str(message.author.id) == ownerID:# or devrole in memberranks:
			msg = remove(message, lang)
		else:
			msg = lang[8]

	elif message.content.startswith(sprefix + "pysetcommand"):
		if permissions.administrator or str(message.author.id) == ownerID:# or devrole in memberranks:
			msg = set(message, lang)
		else:
			msg = lang[8]

	else:
		msg = lang[9]


	return(msg)
