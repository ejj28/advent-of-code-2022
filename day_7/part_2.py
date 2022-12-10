class inode:

    dirTotal = 0
    aboveCandidates = []

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
            return total

    def populateCandidatesAbove(self, above):
        if self.type == "file":
            return self.fileSize
        elif self.type == "dir":
            total = 0
            for i in self.dirChildren:
                total += i.populateCandidatesAbove(above)
            if total >= above:
                inode.aboveCandidates.append(total)
            return total

    def addChild(self, child):
        self.dirChildren.append(child)


rootInode = inode("/", "dir")

path = [] # Path, as dir name strings

def followPath():
    currentNode = rootInode
    for i in path:
       dirs = currentNode.dirChildren
       for dir in dirs:
            if dir.type == "dir" and dir.name == i:
                currentNode = dir
                break
    
    return currentNode

with open("input.txt") as data:
    for rawLine in data.readlines():
        line = rawLine.rstrip()
        if line[0:2] == "$ ":
            if line[2:4] == "cd":
                if line[5:7] == '..':
                    path.pop()
                elif line[5] == '/':
                    path = []
                elif line[5].isalpha():
                    path.append(line[5:len(line)])
            elif line[2:4] == "ls":
                pass
        elif line[0].isnumeric():
            args = line.split(' ')
            newInode = inode(args[1], "file")
            newInode.fileSize = int(args[0])
            followPath().dirChildren.append(newInode)
        elif line[0] == 'd':
            args = line.split(' ')
            newInode = inode(args[1], "dir")
            followPath().dirChildren.append(newInode)
    
    rootTotal = rootInode.getSize()
    rootInode.populateCandidatesAbove((70000000 - (rootTotal + 30000000)) * -1)
    inode.aboveCandidates.sort()
    print(inode.aboveCandidates[0])