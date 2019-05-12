import shiritori

testClass = shiritori.Shiritori('./src/名詞.csv')

testClass.startGame()

while (testClass.gamemode != 0):
    if testClass.gamemode == 1:
        string = input("YourTurn : ")
        print(string)
        result = testClass.inputWord(string)
        if result == -1:
            print("err : try again")
