with open("input.txt") as data:
    containedCounter = 0
    for rawLine in data.readlines():
        line = rawLine.rstrip()
        elfOne, elfTwo = line.split(',')
        elfOne = elfOne.split('-')
        elfTwo = elfTwo.split('-')

        elfOne = [int(elfOne[0]), int(elfOne[1])]
        elfTwo= [int(elfTwo[0]), int(elfTwo[1])]

        print(elfOne,elfTwo)


        if elfTwo[0] >= elfOne[0] and elfTwo[0] <= elfOne[1]:
            containedCounter += 1
        elif elfTwo[1] >= elfOne[0] and elfTwo[1] <= elfOne[1]:
            containedCounter += 1
        elif elfOne[0] >= elfTwo[0] and elfOne[0] <= elfTwo[1]:
            containedCounter += 1
        elif elfOne[1] >= elfTwo[0] and elfOne[1] <= elfTwo[1]:
            containedCounter += 1

    print(containedCounter)