from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def login_user():
    if adharnoEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error ','All Fields Are Required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Root@123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where adharno=%s and password=%s'
        mycursor.execute(query,(adharnoEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Incorrect Adharno or Password')
        else:
            messagebox.showinfo('Welcome','Login Is Sucessfull')
            login_window.destroy()
            import register
    



login_window=Tk()
login_window.geometry('1920x1080')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='image/login page.png')

bgLabel=Label(login_window,image=bgImage)
bgLabel.pack()

heading=Label(login_window,text='User Name',font=('Microsoft Yahei UI Light',23,'bold'),bg='#F5F5F5')
heading.place(x=900,y=300)

adharnoEntry=Entry(login_window,width=22,font=("'Microsoft Yahei UI Light",25))
adharnoEntry.place(x=900,y=350)

heading=Label(login_window,text='Password',font=('Microsoft Yahei UI Light',25,'bold'),bg='#F5F5F5')
heading.place(x=900,y=450)

passwordEntry=Entry(login_window,width=22,show='*',font=("'Microsoft Yahei UI Light",25))
passwordEntry.place(x=900,y=500)

LoginButton=Button(
    login_window,
    text='Login',
    font=('Times', 25),
    command=login_user,
    bg='blue',
    width=10,
    fg='white',
    activebackground='green',
    activeforeground='white'
    ).place(x=1001, y=640)


login_window.mainloop()