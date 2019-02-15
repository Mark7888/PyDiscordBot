def pyhelp(message):
    msg = ""
    msgargs = message.content[1:].split(" ")
    if len(msgargs) == 1:
        msg = """`pyhelp`"""


    return(msg)
