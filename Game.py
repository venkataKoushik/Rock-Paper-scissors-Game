import tkinter
import random
from PIL import ImageTk, Image
#window creation       
window=tkinter.Tk() 
window.geometry("620x350")
window.configure(background="lightgrey")
window.title("Rock Paper Scissors")

#title
title=tkinter.Label(window,text="Rock  Paper  Scissors",font=("Arial",30),fg='black',background="lightgrey")
title.grid(sticky="N",columnspan=3,padx=120)

#setting images 
paper_image=ImageTk.PhotoImage(Image.open("Paper.png"))
scissors_image=ImageTk.PhotoImage(Image.open("Scissor.png"))
rock_image=ImageTk.PhotoImage(Image.open("Rock.png"))

#inserting images in positions
image1=tkinter.Label(window,image=rock_image)
image1.grid(row=1,column=0,padx=10)
user_label=tkinter.Label(window,text="User",background="lightgrey",font=("Arial",15))
user_label.grid(row=2,column=0,padx=10)

image2=tkinter.Label(window,image=paper_image)
image2.grid(row=1,column=2)
user_label=tkinter.Label(window,text="Computer",background="lightgrey",font=("Arial",15))
user_label.grid(row=2,column=2,padx=10)

#function to evalute
def user_choice(x):
    if x==1:
        image1.configure(image=rock_image)
    elif x==2:
        image1.configure(image=paper_image)
    else:
        image1.configure(image=scissors_image)
    y=random.randint(1,3)
    print(y)
    if y==1:
        image2.configure(image=rock_image)
    elif y==2:
        image2.configure(image=paper_image)
    else:
        image2.configure(image=scissors_image)
    if (x==1 and y==1) or (x==2 and y==2) or (x==3 and y==3):
        result=tkinter.Text(window,background="lightgrey",font=("Arial",15),height=1,width=20)
        result.insert(tkinter.END,"          Draw Match")
    elif (x==1 and y==2) or (x==2 and y==3) or (x==3 and y==1):
        result=tkinter.Text(window,background="lightgrey",font=("Arial",15),height=1,width=20,fg='orangered')
        result.insert(tkinter.END,"        Computer Won")
    else:
        result=tkinter.Text(window,background="lightgrey",font=("Arial",15),height=1,width=20,fg='seagreen')
        result.insert(tkinter.END,"            You Won")
    result.grid(row=3,column=1)

#buttons 
rockbutton=tkinter.Button(window,text="Rock",width=9,height=1,bg='yellow',fg='black',command=lambda:user_choice(1))
rockbutton.grid(row=4,column=1,pady=7)
rockbutton=tkinter.Button(window,text="Paper",width=9,height=1,bg='deepskyblue',fg='black',command=lambda:user_choice(2))
rockbutton.grid(row=5,column=1,pady=7)
rockbutton=tkinter.Button(window,text="Scissor",width=9,height=1,bg='violet',fg='black',command=lambda:user_choice(3))
rockbutton.grid(row=6,column=1,pady=7)

window.mainloop()

