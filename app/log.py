from os import makedirs
def log(message, msg, log_prefix):
    # console log
    print(log_prefix + "Message from " + message.author.name + " <" + message.author.id + "> ")
    print(log_prefix + "Message: " + "'" + message.content + "'")
    print(log_prefix + "Sent message: " + "'" + msg + "'")
