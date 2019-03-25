from os import makedirs, path
import datetime

def log(message, msg, log_prefix):
    # logfile
    if not path.exists("../app.log"):
        logfile = open("../app.log", "w").close()
    logfile = open("../app.log", "a", encoding='utf-8')
    # datetime
    time = str(datetime.datetime.now())
    logtime = time[:len(time)-7]
    # console log
    print(log_prefix + "Message from " + message.author.name + " <" + message.author.id + "> ")
    print(log_prefix + "Message: " + "'" + message.content + "'")
    print(log_prefix + "Sent message: " + "'" + msg + "'")

    # log file
    logfile.write(logtime + " - Message from " + message.author.name + " <" + message.author.id + "> \n")
    logfile.write(logtime + " - Message: " + "'" + message.content + "'\n")
    logfile.write(logtime + " - Sent message: " + "'" + msg + "'\n")
    logfile.close()
