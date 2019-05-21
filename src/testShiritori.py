import shiritori

shiritoriClass = shiritori.Shiritori()
ai1 = shiritori.ShiritoriVsComputer("assets/bocchan.csv")
ai2 = shiritori.ShiritoriVsComputer("assets/dogura_magura.csv")

# 人間VSコンピュータ
# while (1):
#     shiritoriClass.inputWord(input("日本語で文字を入れてください "))
#     print(shiritoriClass.usedWords)
#     print(ai1.computerThink(shiritoriClass))
#     print(shiritoriClass.usedWords)
while (shiritoriClass.gamemode == 1):
    print(ai1.computerThink(shiritoriClass))
    print(ai2.computerThink(shiritoriClass))
