import tkinter as tk
import shiritori


shiritoriClass = shiritori.Shiritori()
ai1 = shiritori.ShiritoriVsComputer("assets/dogura_magura.csv")
ai2 = shiritori.ShiritoriVsComputer("assets/dogura_magura.csv")

global count
count = 1

root = tk.Tk()
root.title("しりとり")

countlabel = tk.Label(root, text="{}回目".format(count))
countlabel.pack()

errlabel = tk.Label(root, text="")
errlabel.pack()

nextcharlabel = tk.Label(root, text="")
nextcharlabel.pack()

txt = tk.Entry()
txt.pack()

def pushed():
    r = shiritoriClass.inputWord(txt.get())
    if (r!=0):
        errlabel["text"] = "err {} : 何かしら違うよ♡".format(r)
        return
    else:
        errlabel["text"] = ""

    comp_result = ai1.computerThink(shiritoriClass)
    errlabel["text"] = "{} -> {}".format(txt.get(), comp_result[0])
    nextcharlabel["text"] = "次の文字 {}".format(shiritoriClass.usedWords[-1][-1])

    txt.delete(0, tk.END)
    global count
    count += 1
    countlabel["text"] = "{}回目".format(count)

button = tk.Button(root, text="確定", command=pushed)
button.pack()

root.mainloop()
