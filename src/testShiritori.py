import shiritori

s = shiritori.Shiritori('./assets/bocchan.csv')
print("しりとり")

while (s.gamemode != -1):
    while (True):
        string = input("your turn ")
        result = s.inputWord(string)
        if (result == 0):
            break
        else:
            print("この単語はダメです")
    print("computer turn ", end="")
    print(s.nextWord())
    print(s.usedWords)
    # s.showAllMember()
