# -*- coding: utf-8 -*-
import csv
import MeCab


class Shiritori:
    # プロパティ一覧
    # self.data
    # self.gamemode
    # self.mec
    # self.ngWords
    # self.usedWords
    # self.nextChar
    # dicdata : string(path)
    kana = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰウヱヲーヴガギグゲゴザジズゼゾダヂヅデドバビブベボヷヸヹヺパピプペポ"

    def __init__(self, dictData):
        with open(dictData) as f:
            # 辞書データ
            reader = csv.reader(f)
            self.data = [row for row in reader]
            self.initGame()

    def initGame(self):
        # gamemode
        self.gamemode = 0  # 0 : wait
        # mecab
        self.mec = MeCab.Tagger("-Oyomi")
        # NGword
        self.ngWords = ["ン"]
        # 使われた単語のリスト
        # カタカナ
        self.usedWords = []
        # 次に来る文字
        self.nextChar = ""

    def startGame(self):
        #もしgamemodeが0でない(=すでに始まっている)ならError
        if self.gamemode != 0:
            return -1
        self.initGame()
        self.gamemode = 0  # 1 : player

    def gameOver(self):
        self.gamemode = 0

    def nextWord(self):
        # 次の単語を返す
        return "called nextWord()"

    def inputWord(self, instring):
        # gamemodeの確認
        if self.gamemode == 2:
            return -1
        # 日本語読みの取得
        # 最後の文字は改行文字になるのでカット
        yomi = self.mec.parse(instring)[:-1]
        if (yomi == ""):
            return -2
        # ンで終わる ならば(-1)を返す
        if (yomi[-1] in self.ngWords):
            self.gameOver()
            return -3
        # すでに使われている
        if (yomi in self.usedWords):
            return -4
        # 次の文字に合うか
        if (not self.nextChar == "" and yomi[1] != self.nextChar):
            return -5
        # かな表と照らし合わせる
        if (yomi[-1] not in self.kana):
            return -6
        # 良いならば
        self.usedWords.append(yomi)
        self.nextChar = yomi[-1]
        self.gamemode = 2  # Computer
        print(yomi, self.nextChar)
        return 0

    def showAllMember(self):
            # print("self.data : ", self.data)
            print("self.gamemode : ", self.gamemode)
            print("self.mec", self.mec)
            print("self.ngWords", self.ngWords)
            print("self.usedWords", self.usedWords)
            print("self.nextchar", self.nextChar)
