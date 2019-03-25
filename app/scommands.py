def scommand(message, sprefix):
    msgargs = message.content[1:].split(" ")
    commandname = msgargs[0]
    commandfile = open('../servers/' + message.server.id + '/commands/' + commandname + ".command", "r", encoding='utf-8')
    commandparts = commandfile.read().split("\n")
    msg = commandparts[1]
    return(msg)
