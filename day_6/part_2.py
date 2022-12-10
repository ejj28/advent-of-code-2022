with open("input.txt") as data:
    datastream = data.readline()

    for i in range(len(datastream) - 13):
        slice = datastream[i:i+14]
        prevChars = []
        fail = False
        for char in slice:
            if char in prevChars:
                fail = True
                break
            prevChars.append(char)
        if fail == False:
            print(i+14)
            break