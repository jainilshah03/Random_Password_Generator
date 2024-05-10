from tkinter import*
import string
import random
import pyperclip
def generator():
    small_alphabet = string.ascii_lowercase
    capital_alphabet = string.ascii_uppercase
    numbers_alphabet = string.digits
    special_alphabet = string.punctuation
    all=small_alphabet+capital_alphabet+numbers_alphabet+special_alphabet
    password_length= int(Length_box.get())
    if choice.get()==1:
        passwordfield.insert(0,random.sample(small_alphabet,password_length))
    if choice.get()==2:
        passwordfield.insert(0, random.sample(small_alphabet+capital_alphabet,password_length))
    if choice.get()==3:
        passwordfield.insert(0, random.sample(all,password_length))

    #password=random.sample(all,password_length)
    #passwordfield.insert(0,password)
def copy():
    random_password=passwordfield.get()
    pyperclip.copy(random_password)
root = Tk()
root.config(bg='grey')
choice=IntVar()
Font=('Arial', 18,'bold')
passwordlabel=Label(root,text='Password Generator',font=('times new roman',30,'bold'),bg='grey',fg='white')
passwordlabel.grid(pady=5)
Weakradiobuttton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
Weakradiobuttton.grid(pady=5)
Mediumradiobuttton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
Mediumradiobuttton.grid(pady=5)
Strongradiobuttton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
Strongradiobuttton.grid(pady=5)

lengthlabel=Label(root,text='Password length',font=Font,bg='grey',fg='white')
lengthlabel.grid(pady=5)
Length_box=Spinbox(root,from_=5,to=12,width=5,font=Font)
Length_box.grid(pady=5)

Generaterbuttton=Button(root,text='Generate',font=Font,command=generator)
Generaterbuttton.grid(pady=5)
passwordfield=Entry(root,width=25,bd=2,font=Font)
passwordfield.grid(pady=5)
copybuttton=Button(root,text='Copy',font=Font,command=copy)
copybuttton.grid(pady=5)
root.mainloop()