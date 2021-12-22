from digi import root
def show():
    mydb = dic.connect(host='localhost', user='root', password='', database='csc')
    cur = mydb.cursor()
    cur.execute("SELECT * FROM haryana")
    haryana = cur.fetchall()
    print(haryana)
    i=0
    for i, (Sr_No, Name, Father_Name, Service_Name, Application_Number, Status) in enumerate(haryana, start=1):
        lst.insert("", "end", VALUES(Sr_No, Name, Father_Name, Service_Name, Application_Number, Status))
        mydb.close()

cols= ('Sr_No.', 'Name', 'Father_Name','Service Name','Application_Number','Date','Status')
lst=ttk.Treeview(f6, columns=cols, show="headings")
for col in cols:
    lst.heading(col, text=col)
    lst.pack()
lst.pack()









# from tkinter import *
#
# # from tkinter import ttk
#
# root=Tk()
# root.geometry('500x400')
# root.title('My India Book')
# def register():
#     Label(root, text='Bharat', fg='red', font=('Arial Bold', 20), relief=RIDGE, padx=5).pack(fill=X, padx=10, pady=10)
#     LabelFrame(root, text='  Create an Account  ', height=230, width=460, labelanchor='n').place(x=20, y=130)
#     Label(root, text='First Name', fg='black').place(x=70, y=165)
#     Label(root, text='Last Name', fg='black').place(x=70, y=190)
#     Label(root, text='Gender', fg='black').place(x=70, y=215)
#     Label(root, text='Gmail', fg='black').place(x=70, y=240)
#     Label(root, text='Mobile', fg='black').place(x=70, y=265)
#     Label(root, text='Password', fg='black').place(x=70, y=290)
#     fnvalue = StringVar()
#     lnvalue = StringVar()
#     genvalue = StringVar()
#     gmvalue = StringVar()
#     mobvalue = IntVar()
#     passwvalue = StringVar()
#     fnentry = Entry(root, textvariable=fnvalue, relief=SOLID).place(x=150, y=165)
#     lnentry = Entry(root, textvariable=lnvalue, relief=SOLID).place(x=150, y=190)
#     genentry = Entry(root, textvariable=genvalue, relief=SOLID).place(x=150, y=215)
#     gmentry = Entry(root, textvariable=gmvalue, relief=SOLID).place(x=150, y=240)
#     mobentry = Entry(root, textvariable=mobvalue, relief=SOLID).place(x=150, y=265)
#     passwentry = Entry(root, textvariable=passwvalue, relief=SOLID).place(x=150, y=290)
#     Button(root, text='Register', relief=RIDGE).place(x=150, y=315)
# register()
# root.mainloop()
