with open("input.txt") as data:

    sum = 0

    groups = []
    counter = 0
    group = []

    for rawLine in data.readlines():

        line = rawLine.rstrip()
        group.append(line)
        counter += 1

        if counter == 3:
            groups.append(group)
            counter = 0
            group = []

    for g in groups:
        
        for i in g[0]:
            if i in g[1]:
                if i in g[2]:
                    
                    if i.isupper():
                        sum += ord(i)-38
                    elif i.islower():
                        sum += ord(i)-96
                    break

        
    print(sum)