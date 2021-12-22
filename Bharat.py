from tkinter import *
# from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
# from test import register
import tkinter.messagebox as tm
# import tkinter.messagebox as tmsg
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, column=1)
        self.label_password.grid(row=1)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.place(x=150)

        self.place(x=50, y=20)

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "john" and password == "password":
            tm.showinfo("Login info", "Welcome John")
        else:
            tm.showerror("Login error", "Incorrect username")

root=Tk()
root.geometry("500x400")
root.title("Bharatkibook")
image=Image.open('my.png')
pr=image.resize((70, 80))
fr=ImageTk.PhotoImage(pr)


def raise_frame(frame):
    frame.tkraise()

f1=LabelFrame(root,text='', height=300, width=480, relief=SOLID)
f2=LabelFrame(root,text='', height=300, width=480, relief=SOLID)
f3=LabelFrame(root,text='', height=300, width=480, relief=SOLID)
f4=LabelFrame(root,text='', height=300, width=480, relief=SOLID)
for frame in (f1,f3,f2, f4):
    frame.place(x=10, y=85)

lf = LoginFrame(f2)

Label(root, text="BHARAT", fg='red', font='comicsansms 20 bold', relief=SOLID).pack(padx=10, side=TOP, fill=X,
                                                                                    pady=5)
# def show():

# Label(f2, text='Username', fg='black').place(x=20, y=100)
# Label(f2, text='Password', fg='black').place(x=220, y=100)
# uservalue = StringVar()
# passvalue = StringVar()
# userentry = Entry(f2, textvariable=uservalue, relief=SOLID).place(x=80, y=100)
# passentry = Entry(f2, textvariable=passvalue, relief=SOLID).place(x=280, y=100)
# Button(f2, text='Login', relief=RIDGE, command=lambda: raise_frame(f1)).place(x=420, y=100)
# Button(f2, text='Register', relief=RIDGE, command=register).place(x=420, y=130)


Label(f3, image=fr, relief=SOLID).place(x=90, y=110)
Label(f3, text='Name: ').place(x=200, y=110)
# Label(root, text=fnvalue.get()).place(x=260,y=110)
Label(f3, text='Gender: ').place(x=200, y=130)
Label(f3, text='______________', fg='red', font='comicsansms 9 bold').place(x=250, y=130)
Label(f3, text='Mobile: ').place(x=200, y=150)
Label(f3, text='______________', fg='red', font='comicsansms 9 bold').place(x=250, y=150)
Label(f3, text='Gmail: ').place(x=200, y=170)
Label(f3, text='_______________', fg='red', font='comicsansms 9 bold').place(x=250, y=170)

# thn.return messagebox.showinfo('Success', 'Your Account has been Created', parent=thn)
# thn.showinfo('Thanks', 'Login Successfully')


Button(root, text='Home', relief=RIDGE, command=lambda:raise_frame(f1)).place(x=30, y=50)
Button(root, text="Profile", relief=RIDGE, command=lambda:raise_frame(f3)).place(x=120, y=50)
Button(root, text="Photo", relief=RIDGE, command=lambda:raise_frame(f1)).place(x=210, y=50)
Button(root, text="Login", relief=RIDGE, command=lambda:raise_frame(f2)).place(x=300, y=50)
Button(root, text="Notification", relief=RIDGE, command=lambda:raise_frame(f1)).place(x=400, y=50)
raise_frame(f3)

root.mainloop()
