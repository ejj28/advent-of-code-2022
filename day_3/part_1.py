with open("input.txt") as data:

    sum = 0

    for rawLine in data.readlines():
        line = rawLine.rstrip()
        
        compartmentA = line[0:len(line)//2]
        compartmentB = line[len(line)//2:len(line)]

        match = ""

        for i in compartmentA:
            if i in compartmentB:
                match = i
                break
        
        
        if match.isupper():
            sum += ord(match)-38
        elif match.islower():
            sum += ord(match)-96
        
    print(sum)