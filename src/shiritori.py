# -*- coding: utf-8 -*-
import csv
import MeCab

class Shiritori:
    # dicdata : string(path)
    # プロパティ一覧
    # self.data
    # self.gamemode
    # self.mec
    # self.ngWords
    # self.usedWords
    # self.nextChar
    def __init__(self, dictData):
        with open(dictData) as f:
            # 辞書データ
            reader = csv.reader(f)
            self.data = [row for row in reader]
            self.initGame()
    def initGame(self):
        # gamemode
        self.gamemode = 0 # 0 : wait
        # mecab
        self.mec = MeCab.Tagger("-Oyomi")
        # NGword
        self.ngWords = [ "ン" ]
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
        self.gamemode = 1 # 1 : player
    def gameOver(self):
        self.gamemode = 0
    def nextWord(self):
        # 次の単語を返す
        return "called nextWord()"
    def inputWord(self, instring):
        # gamemodeの確認
        if self.gamemode == 1:
            return -1
        # 日本語読みの取得
        # 最後の文字は改行文字になるのでカット
        yomi = self.mec.parse(instring)[:-1]
        # ンで終わる ならば(-1)を返す
        if (yomi[-1] in self.ngWords):
            self.gameOver()
            return -1
        # すでに使われている
        if (yomi in self.usedWords):
            return -1
        # 次の文字に合うか
        if (self.nextChar!="" or yomi[1]!=self.nextChar):
            return -1
        # 良いならば
        self.usedWords.append(yomi)
        self.nextChar = yomi[1]
        self.gamemode = 2 # Computer
        print(yomi, self.nextChar)

