import shiritori

shiritoriClass = shiritori.Shiritori()
ai = shiritori.ShiritoriVsComputer("assets/bocchan.csv")

while (1):
    shiritoriClass.inputWord(input("日本語で文字を入れてください "))
    print(shiritoriClass.usedWords)
    print(ai.computerThink(shiritoriClass))
    print(shiritoriClass.usedWords)
