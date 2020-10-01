def distance(x, y):
    '''
    :string x:
    :string y:
    :return string:
    '''

    ans = 0
    print("len = ", len(x))
    for idx in range(len(x)):
        ans += (x[idx] != y[idx])
    return str(ans)

# import
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog

# get filepath dialog
root = Tk()
root.filename = filedialog.askopenfilename(initialdir="./", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))

# set mapping character
intab = ""
outtab = "あかさたなはまやらわいきしちにひみりうくすつぬふむゆるんえけせてねへめれおこそとのほもよろをがざだばぱぎじぢびぴぐずづぶぷげぜでべぺごぞどぼぽゃゅょアカサタナハマヤラワイキシチニヒミリウクスツヌフムユルンエケセテネヘメレオコソトノホモヨロヲガザダバパギジジビピグズズブプゲゼデベペゴゾドボポャュョ"
trantab = str.maketrans(intab, outtab)

# convert content and write back
root.content = open(root.filename, "r", encoding='UTF-8').read()
root.newcontent = root.content.translate(trantab)
open(root.filename, "w", encoding='UTF-8').write(root.newcontent)
open(root.filename+"_original", "w", encoding='UTF-8').write(root.content)

# finish message
messagebox.showinfo("Info", "Finish Convert, change " + distance(root.content, root.newcontent) + " character.")
