import shiritori

shiritoriClass = shiritori.Shiritori()
ai1 = shiritori.ShiritoriVsComputer("assets/dogura_magura.csv")
ai2 = shiritori.ShiritoriVsComputer("assets/dogura_magura.csv")
<<<<<<< HEAD
count = 1

# 人間VSコンピュータ
while (1):
    print("\n", count,"回目",sep="")
    r = shiritoriClass.inputWord(input("日本語で文字を入れてください "))
    if (r!=0):
        print("err {} : 何かしら違うよ♡".format(r))
        continue
    comp_result = ai1.computerThink(shiritoriClass)
    print("AIの\t :{}".format(comp_result[0]))
    print("次の文字\t :{}".format(shiritoriClass.usedWords[-1][-1]))
    count += 1
=======
count = 0

# 人間VSコンピュータ
while (1):
    count += 1
    print(count,"回目",sep="")
    shiritoriClass.inputWord(input("日本語で文字を入れてください "))
    print(shiritoriClass.usedWords)
    print(ai1.computerThink(shiritoriClass))
    print(shiritoriClass.usedWords)
>>>>>>> origin/master
# コンピュータVSコンピュータ
# while (shiritoriClass.gamemode == 1):
#     count += 1
#     result1 = ai1.computerThink(shiritoriClass)
#     result2 = ai2.computerThink(shiritoriClass)
#     print(count,"回目",sep="")
#     print("AI 1番 : "+result1[0]+" "+result1[1])
#     print("AI 2番 : "+result2[0]+" "+result2[1])
