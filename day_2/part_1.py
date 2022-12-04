with open("input.txt") as data:

    scores = {"X":1, "Y":2, "Z":3}

    wins = {"X":"C", "Y":"A", "Z":"B"}
    ties = {"X":"A", "Y":"B", "Z":"C"}

    totalScore = 0

    for line in data.readlines():

        roundScore = 0

        them, you = line.split()
        roundScore += scores[you]
        if wins[you] == them:
            roundScore += 6
        elif ties[you] == them:
            roundScore += 3
        
        totalScore += roundScore
    
    print(totalScore)