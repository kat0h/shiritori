import shiritori

shiritoriClass = shiritori.Shiritori()
ai1 = shiritori.ShiritoriVsComputer("assets/dogura_magura.csv")
ai2 = shiritori.ShiritoriVsComputer("assets/dogura_magura.csv")
count = 0

# 人間VSコンピュータ
while (1):
    count += 1
    print(count,"回目",sep="")
    shiritoriClass.inputWord(input("日本語で文字を入れてください "))
    print(shiritoriClass.usedWords)
    print(ai1.computerThink(shiritoriClass))
    print(shiritoriClass.usedWords)
# コンピュータVSコンピュータ
# while (shiritoriClass.gamemode == 1):
#     count += 1
#     result1 = ai1.computerThink(shiritoriClass)
#     result2 = ai2.computerThink(shiritoriClass)
#     print(count,"回目",sep="")
#     print("AI 1番 : "+result1[0]+" "+result1[1])
#     print("AI 2番 : "+result2[0]+" "+result2[1])
