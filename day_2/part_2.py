with open("input.txt") as data:

    scores = {"A":1, "B":2, "C":3}

    # [their move : our move]
    wins = {"A":"B", "B":"C", "C":"A",}
    ties = {"A":"A", "B":"B", "C":"C"}
    loses = {"A":"C", "B":"A", "C":"B"}

    totalScore = 0

    for line in data.readlines():

        roundScore = 0

        them, you = line.split()
        
        yourMove = ""

        if you == 'X': # lose
            yourMove = loses[them]
        elif you == 'Y': # tie
            yourMove = ties[them]
            roundScore += 3
        elif you == 'Z': # win
            yourMove = wins[them]
            roundScore += 6

        roundScore += scores[yourMove]            
        
        totalScore += roundScore
    
    print(totalScore)