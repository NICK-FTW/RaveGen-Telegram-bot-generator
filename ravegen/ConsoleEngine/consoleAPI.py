import signal
import consoleManager as consoleManager
import RaveEngine.projectManager as projectManager
import RaveEngine.botManager as botManager
import CloudEngine.cloudManager as cloudManager
import Utils.inputManager as inputManager
import Utils.utils as utils

def initProgram(argv):
    signal.signal(signal.SIGINT, utils.sigintHandler)
    consoleManager.verifyArgs(argv)
    command = argv[1]

    if command == "help":
        consoleManager.printHelp()
    elif command == "init":
        options = consoleManager.getOptions(argv)
        TOKEN = inputManager.getInput("Bot token (given by @BotFather): ")
        if TOKEN == "":
            TOKEN = None
        if(len(options) == 0):
            projectManager.createInitProject(TOKEN=TOKEN)
        else:
            createBasicModules = False
            for option in options:
                if option == 'm':
                    createBasicModules = True
            projectManager.createInitProject(createBasicModules=createBasicModules, TOKEN=TOKEN)
    elif command == "create":
        options = consoleManager.getOptions(argv)
        testFlag = True
        for option in options:
            if option == 't':
                testFlag = True
            if option == 'd':
                testFlag = False
        botManager.generateBot(testFlag)
    elif command == "deploy":
        options = consoleManager.getOptions(argv)
        if(len(options) == 0):
            botManager.deployBot() 
        else:
            testFlag = True
            for option in options:
                if option == 't':
                    testFlag = True
                if option == 'd':
                    testFlag = False
            botManager.deployBot(withOptions=True, testFlag=testFlag)
    elif command == "change":
        options = consoleManager.getOptions(argv)
        testFlag = True
        for option in options:
            if option == 't':
                testFlag = True
            if option == 'd':
                testFlag = False
        botManager.changeState(testFlag)
    elif command == "deleteCloudBot":
        cloudManager.destroy()


        
        


    






