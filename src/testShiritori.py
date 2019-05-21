import shiritori

shiritori = shiritori.Shiritori()

while (1):
    shiritori.inputWord(input("日本語で文字を入れてください "))
    print(shiritori.usedWords)
