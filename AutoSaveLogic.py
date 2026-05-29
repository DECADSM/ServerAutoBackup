import os, datetime, zipfile

selectedGame = ""
serverPath = ""
backupPath = ""
logBox = ""

def setLogBox(textbox):
    logBox = textbox
    
def SetGame(choice):
    global selectedGame
    selectedGame = choice
    print("Game set: ", selectedGame)
    
def SetServerPath(path, writeFN, backup):
    global serverPath
    global backupPath
    if path:
        if not os.path.exists(path):
            writeFN("This is not a server path\n")
            print("This is not a server path")
            return
        serverPath = path
        writeFN(f"Server Path set: {serverPath}\n")
        print("Server Path set: ", serverPath)
    else:
        writeFN("No server path detected\n")
        print("No server path detected")
        
    if backup:
        backupPath = backup
        writeFN("Backup path given\n")
    else:
        backupPath = ""
    
    
def BackUpDir():
    global backupPath
    if not backupPath:
        backupPath = os.path.join(serverPath, "Backups")
        os.makedirs(backupPath)
        
def GetImportantFiles(writeFN):
    BackUpDir()
    files = []
    match selectedGame:
        case "Minecraft":
            files.append(os.path.join(serverPath, "world"))
            files.append(os.path.join(serverPath, "server.properties"))
            files.append(os.path.join(serverPath, "ops.json"))
            files.append(os.path.join(serverPath, "usercache.json"))
            files.append(os.path.join(serverPath, "user_jvm_args.txt"))
            files.append(os.path.join(serverPath, "config"))
            files.append(os.path.join(serverPath, "mods"))
            files.append(os.path.join(serverPath, "defaultconfigs"))
            files.append(os.path.join(serverPath, "tacz"))
            files.append(os.path.join(serverPath, "tacz_backup"))
            files.append(os.path.join(serverPath, "patchouli_books"))
            files.append(os.path.join(serverPath, "moonlight-global-datapacks"))
            files.append(os.path.join(serverPath, "journeymap"))
            files.append(os.path.join(serverPath, "thingpacks"))
        #case "Vintage Story":
            
        #case "Arma 3":
    for i in files:
        if not os.path.exists(i):
            writeFN(f"{i} does not exsist")
    #writeFN("paths exsist")
    
    time = datetime.datetime.now().strftime("%m-%d-%Y_%Hhr-%Mm")
    with zipfile.ZipFile(os.path.join(backupPath, "Backup_" + time + ".zip"), "w") as backup:
        for file in files:
            backup.write(file, arcname=os.path.basename(file))