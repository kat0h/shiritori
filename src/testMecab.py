import sys
import MeCab

m = MeCab.Tagger("-Oyomi")
'''
mecabインスタンスの生成(出力フォーマットはchasen)
ヨミ：("-Oyomi")
全情報：("-Odump")
わかち書き：("-O wakati")
etc... 公式ドキュメント見てください。
'''

text = input(">>")
print(m.parse(text))
