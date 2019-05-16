import shiritori

s = shiritori.Shiritori('./assets/名詞.csv')

while (s.gamemode != -1):
    while (True):
        string = input("your turn ")
        result = s.inputWord(string)
        if (result == 0):
            break
        else:
            print("この単語はダメです")
    print("computer turn ")
    print(s.nextWord())
    s.showAllMember()
