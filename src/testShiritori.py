import shiritori

s = shiritori.Shiritori('./assets/名詞.csv')

while (s.gamemode != -1):
    while (True):
        string = input("your turn ")
        result = s.inputWord(string)
        if (result != -1):
            break
    print("computer turn ")
    print(s.nextWord())
