import mysql.connector
import tkinter  as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("600x250")
my_connect = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="csc"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM form limit 0,10")
i=0
for form in my_conn:
    for j in range(len(form)):
        e = Entry(my_w, width=15, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, form[j])
    i=i+1
# e = Label(my_w,width=50, text=form[j],
#               borderwidth=2,relief='ridge', anchor="w")
e=Label(my_w,width=15,text='Sr.No',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=0)
e=Label(my_w,width=15,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=1)
e=Label(my_w,width=15,text='Form Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=2)
e=Label(my_w,width=15,text='Form Status',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=3)
e=Label(my_w,width=15,text='Apply Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=4)
my_w.mainloop()