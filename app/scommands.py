from configparser import ConfigParser

def scommand(message, sprefix, devrole, lang, ownerID):

	permissions = message.channel.permissions_for(message.author)

	msgargs = message.content[1:].split(" ")
	commandname = msgargs[0]
	commandfile = open('../servers/' + str(message.guild.id) + '/commands/' + commandname + ".command", "r", encoding='utf-8')
	commandparts = commandfile.read().split("\n")
	if permissions.administrator or str(message.author.id) == ownerID:# or devrole in memberranks:
		msg = commandparts[1]
	else:
		msg = lang[8]
	return(msg)
