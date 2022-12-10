class inode:

    dirTotal = 0

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.fileSize = 0
        self.dirChildren = []

    def getSize(self):
        if self.type == "file":
            return self.fileSize
        elif self.type == "dir":
            total = 0
            for i in self.dirChildren:
                total += i.getSize()
            if total <= 100000:
                inode.dirTotal += total
            print("TOTAL: " + str(total))
            return total

    def addChild(self, child):
        self.dirChildren.append(child)


rootInode = inode("/", "dir")

path = [] # Path, as dir name strings

def followPath():
    print((" "*20) + "PATH:", path)
    currentNode = rootInode
    for i in path:
       dirs = currentNode.dirChildren
       for dir in dirs:
            print((" "*20) + "INODE:", dir.name)
            if dir.type == "dir" and dir.name == i:
                currentNode = dir
                break
    
    return currentNode

with open("input.txt") as data:
    for rawLine in data.readlines():
        line = rawLine.rstrip()
        if line[0:2] == "$ ":
            print("COM", end='')
            if line[2:4] == "cd":
                print(">CD")
                if line[5:7] == '..':
                    print("GO UP")
                    path.pop()
                elif line[5] == '/':
                    print("GO ROOT")
                    path = []
                elif line[5].isalpha():
                    print("GO DIR")
                    path.append(line[5:len(line)])
            elif line[2:4] == "ls":
                print(">LS")
        elif line[0].isnumeric():
            print("FILE")
            args = line.split(' ')
            newInode = inode(args[1], "file")
            newInode.fileSize = int(args[0])
            print("INODE FSIZE")
            print(newInode.fileSize)
            followPath().dirChildren.append(newInode)
            print((" "*20) + followPath().name)
        elif line[0] == 'd':
            print("DIR")
            args = line.split(' ')
            newInode = inode(args[1], "dir")
            followPath().dirChildren.append(newInode)
    print(rootInode.getSize())
    print(inode.dirTotal)