import tkinter as tk
import random
import time
after_id = None
def guwnotest():
    global after_id
    output.configure(fg="limegreen")
    x ="012345789THEMATRIX"
    bufforino = ""
    for i in range (scale.get()):
        bufforino+=random.choice(x)
        trueOutput.set(bufforino)
    
    after_id = root.after(50,guwnotest)
    

root = tk.Tk()
root.geometry("500x500")
root.configure(bg='#242424')
root.title("PasswordMaker")

###
trueOutput = tk.StringVar()

CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
test = 0


def stop():
    global after_id
    if after_id:
        root.after_cancel(after_id)
        after_id = None
    output.configure(fg="white")
    makePassword()

def makePassword():
    test = 0
    test+=1
    letters = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM"
    digits = "1234567890"
    specialSigns = " !@#$%&<>"
    n = scale.get()
    passwordbuffor = ""
    passwordbuffor+=letters
    password = ""


    if(CheckVar1.get()==1):
        passwordbuffor+=digits

    if(CheckVar2.get()==1):
        passwordbuffor+=specialSigns

    for i in range (n):
        password+=str(random.choice(passwordbuffor))
        
    trueOutput.set(password)
###

description = tk.Text(root,bg = "#242424" , width = 30, height = 2,fg = "white",font=("Roboto", 24, "bold"),highlightthickness=0,bd=0)
description.pack()
description.insert(tk.END,"Press the button to \ncreate your password")
description.place(x=100,y=100)

output = tk.Entry(root,state='readonly', textvariable = trueOutput, width = 30,font=("Courier"),readonlybackground='black', fg='white')
output.config(textvariable=trueOutput)
output.pack()

output.place(x=100,y=250)


button = tk.Button(root, width=8,height=4,text = "Click!", command=stop,bd=0)
button.pack()
button.place(x=360,y=375)


digitbutton = tk.Checkbutton(root, text="Do you want to append digits?",font=("Roboto",10, "bold"),variable = CheckVar1,onvalue = 1, offvalue = 0,bg="#242424",fg = 'white',selectcolor="#242424",activebackground = "#242424",activeforeground = "white",highlightthickness=0,bd=0)
digitbutton.pack()
digitbutton.place(x=70,y=380)

specialsignsbutton = tk.Checkbutton(root, text="Do you want to append special signs?",font=("Roboto",10, "bold"),variable = CheckVar2,onvalue = 1, offvalue = 0,bg="#242424",fg = 'white',selectcolor="#242424",activebackground = "#242424",activeforeground = "white",highlightthickness=0,bd=0)
specialsignsbutton.pack()
specialsignsbutton.place(x=70,y=420)

scale = tk.Scale(root, from_ = 0, to = 30, orient=tk.HORIZONTAL,font=("Roboto", 15, "bold"),width = 13,bg = "#242424",fg = "white",bd = 0,length=300,highlightbackground = "#242424",troughcolor="#191919",activebackground="#242424")
scale.pack()
scale.set(15)
scale.place(x=100,y=280)



guwnotest()

root.mainloop()


