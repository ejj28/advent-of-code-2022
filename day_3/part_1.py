import string
with open("input.txt") as data:

    sum = 0

    for line in data.readlines():
        string = line.rstrip()
        
        compartmentA = string[0:len(string)//2]
        compartmentB = string[len(string)//2:len(string)]

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