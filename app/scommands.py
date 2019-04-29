from configparser import ConfigParser

def scommand(message, sprefix, devrole, lang):

    # message author roles
	memberranks = []
	for allrank in message.author.roles:
		memberranks.append(allrank.id)


	msgargs = message.content[1:].split(" ")
	commandname = msgargs[0]
	commandfile = open('../servers/' + message.server.id + '/commands/' + commandname + ".command", "r", encoding='utf-8')
	commandparts = commandfile.read().split("\n")
	if commandparts[2] in memberranks or message.author.server_permissions.administrator or devrole in memberranks:
		msg = commandparts[1]
	else:
		msg = lang[8]
	return(msg)
