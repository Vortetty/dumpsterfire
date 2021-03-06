import sys

f = open(sys.argv[1], "r")

class container:
    def __init__(self, _type):
        self._type = _type
        self.open = False
        self.burnt = False

prntStack = []
burnables = []
curCont = container(None)
usedTypes = []
lineNum = 0
pages = {}


for line in f.readlines():
    parts = line.split()

    parts.append('')

    lineNum += 1

    if parts[0].lower() == "find":
        if curCont.open == False:
            if " ".join(parts[1:]).strip(" ") not in usedTypes:
                curCont = container(" ".join(parts[1:]).strip(" "))
                usedTypes.append(" ".join(parts[1:]).strip(" "))
            else:
                print(f"Error line: {lineNum}, You already burnt this container")
                exit()
        else:
            print(f"Error line: {lineNum}, cannot find a new container without closing current container")
            exit()

    elif parts[0].lower() == "open" and curCont.open == False:
        if curCont.open == False:
            if " ".join(parts[1:]).strip(" ") == curCont._type:
                curCont.open = True
            else:
                print(f"Error line: {lineNum}, specified container must be what you are in")
                exit()
        else:
            print(f"Error line: {lineNum}, cannot open an open container")
            exit()

    elif parts[0].lower() == "write":
        pages[parts[1]] = " ".join(parts[2:]).strip(" ")

    elif parts[0].lower() == "toss":
        if curCont.open == True:
            if curCont.burnt == False:
                if " ".join(parts[2:]).strip(" ") == curCont._type:
                    prntStack.append(pages[parts[1]])
                    pages[parts[1]] = ""
                else:
                    print(f"Error line: {lineNum}, specified container must be what you are in")
                    exit()
            else: 
                print(f"Error line: {lineNum}, cannot toss into a burnt container")
                exit()
        else:
            print(f"Error line: {lineNum}, cannot toss into a closed container")
            exit()
            
    elif parts[0].lower() == "burn":
        if curCont.open == True:
            if " ".join(parts[1:]).strip(" ") == curCont._type:
                for i in prntStack:
                    print(f"[{curCont._type}]: {i}")
                prntStack = []
                curCont.burnt = True
            else:
                print(f"Error line: {lineNum}, specified container must be what you are in")
                exit()
        else:
            print(f"Error line: {lineNum}, cannot burn a closed container")
            exit()

    elif parts[0].lower() == "close":
        if curCont.open == True:
            if curCont.burnt == True:
                if " ".join(parts[1:]).strip(" ") == curCont._type:
                    curCont = container(None)
                else:
                    print(f"Error line: {lineNum}, specified container must be what you are in")
                    exit()
            else:
                print(f"Error line: {lineNum}, cannot close an un-burnt container")
                exit()
        else:
            print(f"Error line: {lineNum}, cannot close a closed container")
            exit()
            