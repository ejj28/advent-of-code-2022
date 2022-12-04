with open("input.txt") as data:
    mostCalories = [0,0,0]
    elfCalories = 0
    for line in data.readlines():
        if line == "\n":
            for elf in range(len(mostCalories)):
                if elfCalories > mostCalories[elf]:
                    mostCalories.insert(elf, elfCalories)
                    mostCalories.pop()
                    break
            elfCalories = 0
        else:
            elfCalories += int(line)
    print(sum(mostCalories))
