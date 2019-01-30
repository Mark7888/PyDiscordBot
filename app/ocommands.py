from reload import reload
def ocommand(message, msgargs, prefix, ownerID, adminID, consol_prefix):
	if message.content.upper().startswith(prefix + "RELOAD"):
		if message.author.id == ownerID:
			reload(message, client, consol_prefix)
	#elif message.content.upper().startswith(prefix + ""):
