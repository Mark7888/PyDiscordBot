commandfile = open("../config/commands.list", "r+")
commandlist = commandfile.read().split(" ")

def pyhelp(message, sprefix, prefix, lang):

    msg = ""
    msgargs = message.content[1:].split(" ")
    # default
    def defaulthelp():
        msg = """ ```css
""" + lang[18] + """
- """ + sprefix + """pyhelp [""" + lang[21] + """]
  /* """ + lang[22] + """ */
- """ + sprefix + """pyaddcommand name=<""" + lang[23] + """>&text=<""" + lang[24] + """>[&description=<""" + lang[25] + """>&rank=<""" + lang[53] + """>]
  /* """ + lang[26] + """ */
- """ + sprefix + """pysetcommand name=<""" + lang[23] + """>[&text=<""" + lang[24] + """>&description=<""" + lang[25] + """>&rank=<""" + lang[53] + """>]
  /* """ + lang[27] + """ */
- """ + sprefix + """pyremovecommand name=<""" + lang[23] + """>
  /* """ + lang[30] + """ */
- """ + sprefix + """pysettings prefix/lang/developer
  /* """ + lang[28] + """ */
- """ + sprefix + """pycommandlist
  /* """ + lang[29] + """ */
- """ + sprefix + """pyclean
  /* """ + lang[31] + """ */
- """ + prefix + """pyprefix
  /* """ + lang[38] + """ */
``` """
        return(msg)

    # addcommand
    def addhelp(lang):
        msg = """ ```css
- """ + sprefix + """pyaddcommand name=<""" + lang[23] + """>&text=<""" + lang[24] + """>[&description=<""" + lang[25] + """>&rank=<""" + lang[53] + """>]
  /* """ + lang[26] + """ */
""" + lang[36] + """ '""" + sprefix + """pyaddcommand name=bot&descriptoin=discord&text=python&rank=7888'
```"""
        return(msg)
    # removecommand
    def removehelp(lang):
        msg = """ ```css
- """ + sprefix + """pyremovecommand name=<""" + lang[23] + """>
  /* """ + lang[30] + """ */
""" + lang[36] + """ '""" + sprefix + """pyremovecommand name=bot'
```"""
        return(msg)
    # setcommand
    def setcommandhelp(lang):
        msg = """ ```css
- """ + sprefix + """pysetcommand name=<""" + lang[23] + """>[&text=<""" + lang[24] + """>&description=<""" + lang[25] + """>&rank=<""" + lang[53] + """>]
  /* """ + lang[27] + """ */
""" + lang[36] + """ '""" + sprefix + """pysetcommand name=bot&text=python&descriptoin=discord&rank=7888'
```"""
        return(msg)
    # settings
    def settingshelp(lang):
        msg = """ ```css
- """ + sprefix + """pysettings
  /* """ + lang[28] + """ */
""" + lang[3] + """
- """ + sprefix + """pysettings prefix <""" + lang[33] + """>
  /* """ + lang[34] + """ */
- """ + sprefix + """pysettings lang <""" + lang[32] + """>
  /* """ + lang[35] + """ */
- """ + sprefix + """pysettings developer @""" + lang[51] + """
  /* """ + lang[52] + """ */
```"""
        return(msg)
    # commandlist
    def listhelp(lang):
        msg = """ ```css
- """ + sprefix + """pycommandlist
  /* """ + lang[29] + """ */
```"""
        return(msg)
    # clean
    def cleanhelp(lang):
        msg = """ ```css
- """ + sprefix + """pyclean
  /* """ + lang[31] + """ */
```"""
    # prefix
    def prefixhelp(lang):
        msg = """ ```css
- """ + prefix + """pyprefix
  /* """ + lang[38] + """ */
```"""
        return(msg)

    # default help
    commandlist.append("pyprefix")
    nothelp = ["pyhelp", "reload"]

    if len(msgargs) == 1:
        msg = defaulthelp()
    elif msgargs[1] not in commandlist or msgargs[1] in nothelp:
        msg = defaulthelp()
    # pyaddcommand
    elif msgargs[1] == "pyaddcommand":
        msg = addhelp(lang)
    # pyremovecommand
    elif msgargs[1] == "pyremovecommand":
        msg = removehelp(lang)
    elif msgargs[1] == "pysetcommand":
        msg = setcommandhelp(lang)
    elif msgargs[1] == "pysettings":
        msg = settingshelp(lang)
    elif msgargs[1] == "pycommandlist":
        msg = listhelp(lang)
    elif msgargs[1] == "pyclean":
        msg = cleanhelp(lang)
    elif msgargs[1] == "pyprefix":
        msg = prefixhelp(lang)
    return(msg)
