def hello():
    print("hello")
    name = str(input())
    if name:
        print("Hello " + str(name))
    else:
        print("Hello World")
    return


def executeCommnad(command):
    if command == "git init":
        print("Repo inited");
    elif command.startswith("git commit"):
        print("commit success");
    elif command == "git show all commit":
        print("show all commits!");
    else:
        print("unknown command");
    return

while 1:
    command = input();
    if command == "exit":
        print("program exited");
        break
    else:
        executeCommnad(command);
