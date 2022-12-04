with open("input.txt") as data:
    mostCalories = 0
    elfCalories = 0
    for line in data.readlines():
        if line == "\n":
            if elfCalories > mostCalories:
                mostCalories = elfCalories
            elfCalories = 0
        else:
            elfCalories += int(line)
    print(mostCalories)
