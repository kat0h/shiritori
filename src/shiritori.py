# -*- coding: utf-8 -*-
# shiritori.py
# made by kato-k (KotaKato)
# 2019 05 17

# stderr
import sys
# MeCab が必要です
import MeCab

# for ShiritoriAi
import csv
import random

class Shiritori:
    kana = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰウヱヲヴガギグゲゴザジズゼゾダヂヅデドバビブベボヷヸヹヺパピプペポ"
    def __init__(self):
        # mecab
        self.mec = MeCab.Tagger("-Oyomi")
        # NGword
        self.ngWords = ["ン"]
        # 使われた単語のリスト
        # カタカナ
        self.usedWords = []
        # 次に来る文字
        self.nextChar = ""
        self.gamemode = 1
    # 入力を確認＋反映
    # 戻り値: 0   完了
    #         -1  不正
    def checkWord(self, word, isSilent=True):
        # 読みのチェック
        if (word == ""):
            if (isSilent == False):
                sys.stderr.write("Err : Word is empty\n")
            return -1
        # ンで終わる ならば(-1)を返す
        if (word[-1] in self.ngWords):
            if (isSilent == False):
                sys.stderr.write("Err : NGWord (example 'ン')\n")
            return -2
        # すでに使われている
        if (word in self.usedWords):
            if (isSilent == False):
                sys.stderr.write("Err : Word was used\n")
            return -3
        # 次の文字に合うか
        if (not self.nextChar == "" and word[0] != self.nextChar):
            if (isSilent == False):
                sys.stderr.write("Err : Word is not match nextChar\n")
            return -4
        # かな表と照らし合わせる
        if (word[-1] not in self.kana):
            if (isSilent == False):
                sys.stderr.write("Err : Word is not in kana table\n")
            return -5
        return 0
    # input : kana
    def refrection(self, word):
        self.usedWords.append(word)
        self.nextChar = word[-1]
    def inputWord(self, instring):
        # 日本語読みの取得
        # 最後の文字は改行文字になるのでカット
        yomi = self.mec.parse(instring)[:-1]
        # 読みのチェック
        if (self.checkWord(yomi) != 0):
            return -1
        self.refrection(yomi)
        # print(yomi, self.nextChar)
        return 0

class ShiritoriVsComputer:
    def __init__(self, path):
        with open(path) as f:
            # 辞書データ
            reader = csv.reader(f)
            self.data = [row for row in reader]
    def computerThink(self, shiritoriclass :Shiritori):
        # 次の単語を確認
        num = []
        # 使えるデータを探す
        for i in range(len(self.data)):
            # 次の文字で始まっていて、使われた単語に入っていない
            if (shiritoriclass.checkWord(self.data[i][1], True) == 0):
                num.append(i)
        if (num == []):
            shiritoriclass.gamemode = -1 #終了
            return -1
        # 消す
        # print(num)
        n = num[random.randrange(0, len(num))]
        if (shiritoriclass.inputWord(self.data[n][1]) == 0):
            ret = self.data.pop(n)
            # 次の単語を返す
            return ret
        else:
            return ["",""]
