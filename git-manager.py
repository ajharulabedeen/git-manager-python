class commit:
    def __init__(self, id, message):
        self.id = id
        self.message = message


def addCommit(command):
    split = command.split();
    message = '';
    for counter in range(len(split)):
        if counter > 1:
            message += split[counter] + " ";
    listCommit.append(commit(commandCounter, message))
    print("commit success");

def deleteCommit(command):
    split = command.split();
    deleteID = split[2];
    for obj in listCommit:
        if obj.id == int(deleteID):
            listCommit.remove(obj);
    print("delete success")


def executeCommnad(command):
    if command == "git init":
        print("Repo inited");
    elif command.startswith("git commit"):
        addCommit(command)
    elif command == "git show all commit":
        for obj in listCommit:
            print(obj.id, obj.message, sep=' ')
    elif command.startswith("git delete"):
        deleteCommit(command)
    else:
        print("unknown command");
    return

listCommit = [];
commandCounter = 0;
while 1:
    command = input();
    commandCounter += 1;
    if command == "exit":
        print("program exited");
        break
    else:
        executeCommnad(command);
