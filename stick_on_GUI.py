from tkinter import *
from tkinter import messagebox
def btn():
    y=int(text.get())
    btn.config(state='disabled')
    btn1.config(state='normal')
    z=int(text2.get())
    if y<=4 and y>=1:
     if (z-y)<0:
         messagebox.showerror("error" , "please enter less than of total stick")
         btn.config(state='normal')
         btn1.config(state='disabled')
     else:
        q=z-y
        s.set(q)
    else:
        btn.config(state='normal')
        btn1.config(state='disabled')
        messagebox.showerror("error" , "please enter b/w 1 to 4")
    try:
     if q==0:
        btn.config(state='disabled')
        btn1.config(state='disabled')
        text2.config(state='disabled')
        messagebox.showinfo("Winner" ,"Player B")
    except:
        pass
        
def btn2():
    t=int(text1.get())
    btn.config(state='normal')
    btn1.config(state='disabled')
    b=int(text2.get())
    if t<=4 and t>=1:
     if (b-t)<0:
         messagebox.showerror("error" , "please enter less than of total stick")
         btn1.config(state='normal')
         btn.config(state='disabled')
     else:
        k=b-t
        s.set(k)
    else:
        btn1.config(state='normal')
        btn.config(state='disabled')
        messagebox.showerror("error" ,"please enter b/w 1 to 4")
    try:
     if k==0:
        btn.config(state='disabled')
        btn1.config(state='disabled')
        text2.config(state='disabled')
        messagebox.showinfo("Winner" ,"Player A")
    except:
        pass
root=Tk()
root.title("STICK MIND")
fr=Frame(root ,bg="black")

frame1=Label(root , text="STICK MIND", font="arial 16 bold" ,bg="light blue")
frame1.pack()
#Player A ######################
frame2=Label(root ,text="Player A", font="arial 15 bold"  )
text=Entry(root)
text.place(x=4,y=100)
frame2.place(x=4,y=60)
btn=Button(root, text="submit" ,command=btn)
btn.place(x=4,y=140)
    
#player B #########################
frame3=Label(root ,text="Player B", font="arial 15 bold" )
text1=Entry(root)
text1.place(x=370,y=100)
frame3.place(x=395,y=60)
btn1=Button(root, text="submit" , command=btn2)
btn1.place(x=435,y=140)

#total stick #################
frame4=Label(root ,text="Total stick", font="arial 15 bold" )
s=StringVar()
text2=Entry(root ,textvariable=s )
s.set(21)
text2.place(x=170 ,y=100)
frame4.place(x=180,y=60)

#about game ####################
f1=Label(root , text="ABOUT GAME", font="arial 16 bold" ,bg="light blue")
f1.place(x=170,y=250)
t=Label(root ,text=" hey this is about page ."
        " \n It is A Two Player Game. In This Game We have 21 Sticks."
        " \n Each Players can choose between 1- 4"
        " \n Sticks at a Time. Player Picking up the last \n Stick will loss As per game rules!"
        "\n"
        "\n"
        "\n"
        "\n"
        "\n @Made by Rahul Mars "
                       ,font= "arial 12 bold"  )
t.place(x=25 , y=300)
fr.pack(fill=BOTH)
root.geometry("500x500")
root.resizable(FALSE,FALSE)
root.mainloop()
