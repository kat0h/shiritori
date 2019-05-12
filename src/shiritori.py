# -*- coding: utf-8 -*-
import csv
# MeCab が必要です
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
    kana = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰウヱヲヴガギグゲゴザジズゼゾダヂヅデドバビブベボヷヸヹヺパピプペポ"
    def __init__(self, dictData):
        with open(dictData) as f:
            # 辞書データ
            reader = csv.reader(f)
            self.data = [row for row in reader]
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
        self.gamemode = 0  # 1 : player
    def refrection(self, string):
        self.usedWords.append(string)
        self.nextChar = string[-1]
        return 0
    def nextWord(self):
        # 次の単語を確認
        num = -1
        for i in range(len(self.data)):
            if (self.data[i][1].startswith(self.nextChar) and self.data[i][1] not in self.usedWords):
                nonlocal num
                num = i
                break
            self.usedWords.append(self.data[num][1])
        if (num == -1):
            self.gamemode = -1 #終了
            return -1
        # 消す
        ret = self.data.pop(num)
        # 次の単語を返す
        self.refrection(ret)
        self.gamemode = 1
        return ret
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
        self.refrection(yomi)
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
