with open("input.txt") as data:
    stackMode = True
    stackLines = []
    inputLines = []
    for rawLine in data.readlines():
        line = rawLine.rstrip()
        if stackMode == True:
            if line == "":
                stackMode = False
            else:
                stackLines.append(line)
        else:
            inputLines.append(line)

    # Get indexes of actual values
    indexes = []
    lastRow = stackLines[len(stackLines) - 1]
    
    for i in range(len(lastRow)):
        if lastRow[i].isnumeric():
            indexes.append(i)

    # Create clean 2d list
    cleanStackLines = []

    for line in stackLines:
        
        newRow = []
        for i in indexes:
            
            if i <= len(line) - 1:
                newRow.append(line[i])
            else:
                newRow.append(' ') # Padding for easier rotation
        cleanStackLines.append(newRow)
        
    # Remove label line
    cleanStackLines.pop()

    # Rotate grid

    rotatedGrid = []
    for column in range(len(cleanStackLines[0])):
        newRow = []
        for row in range(len(cleanStackLines)):
            newRow.insert(0, cleanStackLines[row][column])
        rotatedGrid.append(newRow)    
    
    # Remove whitespace
    finalGrid = []
    for row in rotatedGrid:
        newRow = []
        for column in row:
            if column != ' ':
                newRow.append(column)
        finalGrid.append(newRow)
    
    # Perform moves
    for line in inputLines:
        command = line.split(' ')
        
        count = int(command[1])
        toStack = int(command[5]) - 1
        fromStack = int(command[3]) - 1

        for i in range(count):
            finalGrid[toStack].append(finalGrid[fromStack].pop())
            
    # Print result
    for line in finalGrid:
        print(line[len(line) - 1], end='')
