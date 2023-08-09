import random
from tkinter import *

p1 = 0
p2 = 0


def grn():#Generation of number
    global num
    while True:
        num = random.randint(1000, 9999)
        snum=set(str(num))
        if len(snum)==4:
            print(num)
            break

def Singlecondition():  # Condition for Single player
    global p1
    p1 += 1
    c = 0
    b = 0
    innum = Entrypoint1.get()
    if len(str(innum)) == 4:
        for i in range(4):
            if str(innum)[i] == str(num)[i]:
                b += 1
            elif str(innum)[i] in str(num):
                c += 1
        return c, b
    else:
        lerror = Label(window, text="ERROR PLEASE Enter a 4 digit number")
        lerror.pack()


def Multicondition():  # Condition for Multiple Players
    global p2
    p2 += 1
    c1 = 0
    b1 = 0
    c2 = 0
    b2 = 0
    innum1 = Entrypoint2.get()
    innum2 = Entrypoint3.get()
    if len(str(innum1)) == 4 and len(str(innum2)) == 4:
        for i in range(4):
            if str(innum1)[i] == str(num)[i]:
                b1 += 1
            elif str(innum1)[i] in str(num):
                c1 += 1
            if str(innum2)[i] == str(num)[i]:
                b2 += 1
            elif str(innum2)[i] in str(num):
                c2 += 1
        return c1, b1, c2, b2
    else:
        lerror = Label(window, text="ERROR PLEASE Enter a 4 digit number")
        lerror.pack()


def Singledisplay():  # Display for Single player
    t = Singlecondition()
    global l10
    l10=Label(window,text=f"Number of tries  {p1}").place(x=360,y=200)
    if p1 <= 7:
        if (t[1]) == 4:
            

            l1 = Label(window, text="Correct Guess\nGAME OVER", fg='red', font=("Courier New", 20, 'bold'))
            l1.place(x=300, y=300)
            l3 = Label(window, text=t[0], font=("Trebuchet MS", 25, 'bold')).place(x=213, y=400)
            l4 = Label(window, text=t[1], bg='red', font=("Trebuchet MS", 25, 'bold')).place(x=565, y=400)
            Entrybutton1["text"] = "QUIT"
            Entrybutton1["command"] = quit
        else:
            l10=Label(window,text=f"Number of tries  {p1}").place(x=360,y=200)
            l2 = Label(window, text="Unsuccessful", font=("Courier New", 20, 'bold'))
            l3 = Label(window, text=t[0], font=("Trebuchet MS", 25, 'bold')).place(x=213, y=400)
            l4 = Label(window, text=t[1], bg='red', font=("Trebuchet MS", 25, 'bold')).place(x=565, y=400)
            Entrybutton1["text"] = "Try Again"
            l2.place(x=310, y=300)
    elif p1==8:
        l10.place_forget()
        l11=Label(window,text="Last Try").place(x=340,y=200)
        
        
    else:
        clabel = Label(window, text="Number of tries exceeded")
        Entrybutton1["text"] = "Quit"
        Entrybutton1["command"] = quit
        clabel.pack()

def Multidisplay():  # Display for Multiplayer
    if p2 <= 7:
        t = Multicondition()
        if (t[1]) == 4 and t[3] == 4:
            l4 = Label(window, text="Tie\nBOTH WIN!!!" ,font=("Courier New", 20, 'bold'))
            l4.place(x=315, y=300)
            l5 = Label(window, text=t[0], font=("Trebuchet MS", 25, 'bold')).place(x=213, y=380)
            l6 = Label(window, text=t[1], bg='red', font=("Trebuchet MS", 25, 'bold')).place(x=565, y=380)
            l8 = Label(window, text=t[3], bg='white', font=("Trebuchet MS", 25, 'bold')).place(x=565, y=430)
            l7 = Label(window, text=t[2], bg='red', font=("Trebuchet MS", 25, 'bold')).place(x=213, y=430)
            Entrybutton2["text"] = "Quit"
            Entrybutton2["command"] = quit
        elif (t[3]) == 4:
            l1 = Label(window, text="Player 2 Wins\nGAME OVER", fg='red', font=("Courier New", 20, 'bold'))
            l1.place(x=300, y=300)
            l5 = Label(window, text=t[0], font=("Trebuchet MS", 25, 'bold')).place(x=213, y=380)
            l6 = Label(window, text=t[1], bg='red', font=("Trebuchet MS", 25, 'bold')).place(x=565, y=380)
            l8 = Label(window, text=t[3], bg='white', font=("Trebuchet MS", 25, 'bold')).place(x=565, y=430)
            l7 = Label(window, text=t[2], bg='red', font=("Trebuchet MS", 25, 'bold')).place(x=213, y=430)
            Entrybutton2["text"] = "QUIT"
            Entrybutton2["command"] = quit
        elif t[1] == 4:
            l3 = Label(window, text="Player 1 Wins\nGAME OVER", fg='red', font=("Courier New", 20, 'bold'))
            l3.place(x=300, y=300)
            l5 = Label(window, text=t[0], font=("Trebuchet MS", 25, 'bold')).place(x=213, y=380)
            l6 = Label(window, text=t[1], bg='red', font=("Trebuchet MS", 25, 'bold')).place(x=565, y=380)
            l8 = Label(window, text=t[3], bg='white', font=("Trebuchet MS", 25, 'bold')).place(x=565, y=430)
            l7 = Label(window, text=t[2], bg='red', font=("Trebuchet MS", 25, 'bold')).place(x=213, y=430)
            Entrybutton2["text"] = "QUIT"
            Entrybutton2["command"] = quit
        else:
            l5 = Label(window, text=t[0], font=("Trebuchet MS", 25, 'bold')).place(x=213, y=380)
            l6 = Label(window, text=t[1], bg='red', font=("Trebuchet MS", 25, 'bold')).place(x=565, y=380)
            l8 = Label(window, text=t[3], bg='white', font=("Trebuchet MS", 25, 'bold')).place(x=565, y=430)
            l7 = Label(window, text=t[2], bg='red', font=("Trebuchet MS", 25, 'bold')).place(x=213, y=430)
            Entrybutton2["text"] = "Try Again"
    else:
        clabel = Label(window, text="Number of tries exceeded")
        clabel.pack()
        Entrybutton2["text"] = "Quit"
        Entrybutton2["command"] = quit
grn()


def Singleplayer():  # GUI for Singleplayer
    button2.place_forget()
    global Entrypoint1
    Entrypoint1 = Entry(window, width=8,font=('Arial 24',14,'bold') ,justify=RIGHT)
    Entrypoint1.place(x=362, y=500)
    global Entrybutton1
    Entrybutton1 = Button(window, text="Enter", bg='white', fg='black', font=("Tahoma", 15, "bold"),
                          command=Singledisplay)
    Entrybutton1.place(x=540, y=540)


def Multiplayer():  # GUI for Multiple players
    button1.place_forget()
    button2.place(x=320, y=400)
    global Entrypoint2
    Entrypoint2 = Entry(window, width=8,font=('Arial 24',14,'bold') ,justify=RIGHT)
    Entrypoint2.place(x=360, y=500)
    global Entrybutton2
    Entrybutton2 = Button(window, text="Enter", bg='white', fg='black', font=("Tahoma", 15, "bold"),
                          command=Multidisplay)
    Entrybutton2.place(x=540, y=540)
    global Entrypoint3
    Entrypoint3 = Entry(window, width=8,font=('Arial 24',14,'bold'), justify=RIGHT)
    Entrypoint3.place(x=360, y=580)


def change():
    button1["text"] = "SinglePlayer"
    button2['text'] = "MultiPlayer"
    button1["command"] = Singleplayer
    button1.place(x=310, y=400)
    button2.place(x=320, y=500)
    button2["command"] = Multiplayer

#main GUI starts here
window = Tk()
window.title('Bulls and Cows')
window.geometry("800x800")
backgroundimage = PhotoImage(
    file=r"C:\Users\Atharv\OneDrive\Desktop\Bulls and Cows\Images\fire(2).png")
backgroundimagelabel = Label(window, image=backgroundimage)
backgroundimagelabel.place(x=0, y=0)
c = Canvas(window, width=550, height=550, bg='black')
label1 = Label(window, text="Bulls and Cows", bg='black',fg='red', relief='solid', font=("Brush Script MT", 30, "bold"),
               )
label1.pack(fill=BOTH, pady=2, padx=2)


button1 = Button(window, text="Begin", fg='red', bg='white', relief=RIDGE, font=("arial", 20, "bold"),
                 command=change)  # the grn function is called
button1.place(x=350, y=400)
# relief-GROOVE,SUNKEN,RAISED
button2 = Button(window, text="Quit", fg='red', bg='white', relief=RIDGE, font=("arial", 20, "bold"), command=quit)
button2.place(x=360, y=500)
button3image = PhotoImage(file=r"C:\Users\Atharv\OneDrive\Desktop\Bulls and Cows\Images\cowlogo.png")
button3 = Button(window, image=button3image, bg='black', relief='solid', height=150, width=150)
button3.place(x=150, y=200)
button4image = PhotoImage(file=r"C:\Users\Atharv\OneDrive\Desktop\Bulls and Cows\Images\bullogo.png")
button4 = Button(window, image=button4image, bg='black', relief='solid', height=150, width=150)
button4.place(x=500, y=200)
c.place(x=130, y=150)
# window.wm_attributes('-transparentcolor','grey')
window.mainloop()