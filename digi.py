from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as dic
root = Tk()
root.geometry("1000x600")
# root.config(bg="grey")
root.maxsize(width=1100, height=600)
root.minsize(width=1100, height=600)
# root.iconphoto(True, PhotoImage(file="logo.png"))
root.title("Digital Sewa Kendra, Pur")
hr = Image.open("harihar.png")
baba = hr.resize((300, 300))
bh = ImageTk.PhotoImage(baba)
image = Image.open("csc.png")
lg = Image.open("logo.png")
myph = Image.open("my.png")
bnt = Image.open("Bintu.png")
bintu = bnt.resize((105, 120))
bj = ImageTk.PhotoImage(bintu)
myrs = myph.resize((105, 120))
myp = ImageTk.PhotoImage(myrs)
reslg = lg.resize((40, 40))
pl = ImageTk.PhotoImage(reslg)
resimg = image.resize((200, 90))
photo = ImageTk.PhotoImage(resimg)
f2 = LabelFrame(root, borderwidth=2)
f2.pack(pady=10)
plg = Label(f2, image=pl)
plg.pack(side=LEFT)
f1 = LabelFrame(root, width=550, relief=SOLID, bg="yellow", height=308)
f1.place(x=545, y=72)
Label(f1, text='Saral Haryana Data', font="comicsansms 15 bold", bg="yellow", fg="black", relief=RIDGE, highlightthickness= 2, padx=5).place(x=25, y=5)
# Button(root, text="Home", relief=RIDGE).pack(side=TOP)
f5 = LabelFrame(root, height=300, relief=SOLID)
f5.pack(padx=10, anchor="nw")
Label(f5, image=bh).pack(side=LEFT, padx=110)
# f3=LabelFrame(root, text=" Preview ", height=153)
# f3.pack(fill="both", padx=10)
f4 = LabelFrame(root)
f4.pack(side=BOTTOM, anchor="sw", pady=10, padx=35)
csc = Label(root, image=photo)
csc.pack(side=BOTTOM, anchor="sw", padx=180)
f6 = LabelFrame(root, relief=SOLID, height=200, width=550, bg='green')
f6.place(x=545, y=390)
Label(root, image=myp, relief=RAISED).place(x=40, y=420)
Label(root, image=bj, relief=RAISED).place(x=400, y=420)
name = Label(f1, text="Name", bg="yellow")
name.place(x=10, y=50)
fname = Label(f1, text="Father/Hus Name", bg="yellow")
fname.place(x=10, y=75)
sname = Label(f1, text="Service Name", bg="yellow")
sname.place(x=10, y=100)
appln = Label(f1, text="Application No.", bg="yellow")
appln.place(x=10, y=125)
sts = Label(f1, text="Status", bg="yellow")
sts.place(x=10, y=150)
date = Label(f1, text="Submiting Date", bg="yellow")
date.place(x=10, y=175)
namevalue = StringVar()
fthrnamevalue = StringVar()
snamevalue = StringVar()
apvalue = StringVar()
stsvalue = StringVar()
datevalue = StringVar()
namentry = Entry(f1, relief=RIDGE, textvariable=namevalue, borderwidth=2)
namentry.place(x=120, y=50)
fthname = Entry(f1, relief=RIDGE, textvariable=fthrnamevalue, borderwidth=2)
fthname.place(x=120, y=75)
sentry = Entry(f1, relief=RIDGE, textvariable=snamevalue, borderwidth=2)
sentry.place(x=120, y=100)
apentry = Entry(f1, relief=RIDGE, textvariable=apvalue, borderwidth=2)
stentry = Entry(f1, relief=RIDGE, textvariable=stsvalue, borderwidth=2)
apentry.place(x=120, y=125)
stentry.place(x=120, y=150)
datentry = DateEntry(f1, relief=RIDGE, selectmode='day', textvariable=datevalue)
datentry.place(x=120, y=175)


def getval():
    if namevalue.get()=="" or fthrnamevalue.get()=="" or stsvalue.get()=='' or apvalue.get()=='' or snamevalue.get()=='':
        messagebox.showerror("Error",'Sorry!')
    else:
        try:
            mydb = dic.connect(host='localhost', user='root', password='', database='csc')
            s = "INSERT INTO haryana (Name, Father_Name, Service_Name, Application_Number,Submission_Date, " \
                "Status) VALUES(%s, %s, %s, %s, %s, %s) "
            val = (namevalue.get(), fthrnamevalue.get(), snamevalue.get(), apvalue.get(), datevalue.get(), stsvalue.get())
            cur = mydb.cursor()
            cur.execute(s, val)
            mydb.commit()
            # lastid = cur.lastrowid
            messagebox.showinfo('Information', 'Record Saved Successfully!')

            namentry.delete(0, END)
            fthname.delete(0, END)
            sentry.delete(0, END)
            apentry.delete(0, END)
            stentry.delete(0, END)
            namentry.focus_set()
        except Exception as e:
            print(e)
            mydb.rollback()
            mydb.close()


submit = Button(f1, text="Submit", relief=RIDGE,  command=getval)
submit.place(x=120, y=200)

Label(f1, text='Online Form Data', font="comicsansms 15 bold", bg="yellow", fg="black", relief=RIDGE, highlightthickness= 2, padx=5).place(x=300, y=30)
fname = Label(f1, text="Name", bg="yellow")
fname.place(x=300, y=80)
forname = Label(f1, text="Form Name", bg="yellow")
forname.place(x=300, y=105)
fsname = Label(f1, text="Form Status", bg="yellow")
fsname.place(x=300, y=130)
# appln = Label(f1, text="Application No.", bg="yellow")
# appln.place(x=300, y=125)
# sts = Label(f1, text="Status", bg="yellow")
# sts.place(x=300, y=150)
date = Label(f1, text="Submiting Date", bg="yellow")
date.place(x=300, y=155)
frnamevalue = StringVar()
fornamevalue = StringVar()
fsnamevalue = StringVar()
# apvalue = StringVar()
fstsvalue = StringVar()
fdatevalue = StringVar()
fnamentry = Entry(f1, relief=RIDGE, textvariable=frnamevalue, borderwidth=2)
fnamentry.place(x=400, y=80)
fornamentry = Entry(f1, relief=RIDGE, textvariable=fornamevalue, borderwidth=2)
fornamentry.place(x=400, y=105)
fsentry = Entry(f1, relief=RIDGE, textvariable=fsnamevalue, borderwidth=2)
fsentry.place(x=400, y=130)
# apentry = Entry(f1, relief=RIDGE, textvariable=apvalue, borderwidth=2)
# stentry = Entry(f1, relief=RIDGE, textvariable=stsvalue, borderwidth=2)
# apentry.place(x=410, y=125)
# stentry.place(x=410, y=150)
fdatentry = DateEntry(f1, relief=RIDGE, selectmode='day', textvariable=fdatevalue)
fdatentry.place(x=400, y=155)


def form():
    mydb = dic.connect(host='localhost', user='root', password='', database='csc')
    try:
        s = "INSERT INTO form (Name,Form_Name, Form_Status, Date) VALUES(%s, %s, %s, %s)"
        val = (frnamevalue.get(), fornamevalue.get(), fsnamevalue.get(), fdatevalue.get())
        cur = mydb.cursor()
        cur.execute(s, val)
        mydb.commit()
# lastid = cur.lastrowid
        messagebox.showinfo('Information', 'Record Saved Successfully!')

        fnamentry.delete(0, END)
        fornamentry.delete(0, END)
        fsentry.delete(0, END)
        # apentry.delete(0, END)
        # stentry.delete(0, END)
        fnamentry.focus_set()
    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


submit = Button(f1, text="Submit", relief=RIDGE,  command=form)
submit.place(x=400, y=185)


Label(f6, text='Document Data', font="ArialBlack 15 bold", bg="green", fg="white", relief=RIDGE, highlightthickness= 2, padx=5).place(x=25, y=5)
foldername = Label(f6, text="Folder Name", bg="green", fg='gold')
foldername.place(x=10, y=50)
folderlocation = Label(f6, text="Folder Location", bg="green", fg='gold')
folderlocation.place(x=10, y=75)
systemname = Label(f6, text="System Name", bg="green", fg='gold')
systemname.place(x=10, y=100)
foldervalue=StringVar()
folderlocvalue=StringVar()
systemvalue=StringVar()
folderentry = Entry(f6, relief=RIDGE, textvariable=foldervalue, borderwidth=2)
folderentry.place(x=120, y=50)
folderlocentry = Entry(f6, relief=RIDGE, textvariable=folderlocvalue, borderwidth=2)
folderlocentry.place(x=120, y=75)
systementry = Entry(f6, relief=RIDGE, textvariable=systemvalue, borderwidth=2)
systementry.place(x=120, y=100)

def document():
    mydb = dic.connect(host='localhost', user='root', password='', database='csc')
    try:
        s = "INSERT INTO document (Folder_Name,Folder_Location, System_Name) VALUES(%s, %s, %s)"
        val = (foldervalue.get(), folderlocvalue.get(), systemvalue.get())
        cur = mydb.cursor()
        cur.execute(s, val)
        mydb.commit()
# lastid = cur.lastrowid
        messagebox.showinfo('Information', 'Record Saved Successfully!')

        folderentry.delete(0, END)
        folderlocentry.delete(0, END)
        systementry.delete(0, END)
        # apentry.delete(0, END)
        # stentry.delete(0, END)
        folderentry.focus_set()
    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()
Button(f6, text="Submit", relief=RIDGE, command=document).place(x=120, y=130)

Label(f6, text='Payment Record', font="comicsansms 15 bold", bg="green", fg="white", relief=RIDGE, highlightthickness= 2, padx=5).place(x=320, y=5)
custname = Label(f6, text="Name", bg="green", fg='white')
custname.place(x=300, y=50)
total = Label(f6, text="Total Payment", bg="green", fg='white')
total.place(x=300, y=75)
deposit = Label(f6, text="Deposit", bg="green", fg='white')
deposit.place(x=300, y=100)
pending=Label(f6, text='Pending', bg='green', fg='white')
pending.place(x=300, y=125)
custvalue=StringVar()
totalvalue=IntVar()
depositevalue=IntVar()
pendingvalue=IntVar()
custentry = Entry(f6, relief=RIDGE, textvariable=custvalue, borderwidth=2)
custentry.place(x=400, y=50)
totalentry = Entry(f6, relief=RIDGE, textvariable=totalvalue, borderwidth=2)
totalentry.place(x=400, y=75)
depositentry = Entry(f6, relief=RIDGE, textvariable=depositevalue, borderwidth=2)
depositentry.place(x=400, y=100)
pendingentry=Entry(f6, relief=RIDGE, textvariable=pendingvalue, borderwidth=2)
pendingentry.place(x=400, y=125)
def payment():
    mydb = dic.connect(host='localhost', user='root', password='', database='csc')
    try:
        s = "INSERT INTO payment (Name,Total_Payment, Deposit, Pending) VALUES(%s, %s, %s, %s)"
        val = (custvalue.get(), totalvalue.get(), depositevalue.get(), pendingvalue.get())
        cur = mydb.cursor()
        cur.execute(s, val)
        mydb.commit()
# lastid = cur.lastrowid
        messagebox.showinfo('Information', 'Record Saved Successfully!')

        custentry.delete(0, END)
        totalentry.delete(0, END)
        depositentry.delete(0, END)
        pendingentry.delete(0, END)
        # stentry.delete(0, END)
        custentry.focus_set()
    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()

Button(f6, text="Submit", relief=RIDGE,  command=payment).place(x=400, y=150)
def show():
    import mysql.connector
    my_w = Toplevel(root)
    my_w.geometry("600x250")
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="csc"
    )
    my_conn = my_connect.cursor()
    ####### end of connection ####
    my_conn.execute("SELECT * FROM form limit 0,100")
    i = 0
    for form in my_conn:
        for j in range(len(form)):
            e = Entry(my_w, width=15, fg='blue')
            e.grid(row=i, column=j)
            # e.grid(row=1, column=0)
            e.insert(END, form[j])
        i = i + 1
    # e = Label(my_w,width=50, text=form[j],
    #               borderwidth=2,relief='ridge', anchor="w")
    e = Label(my_w, width=15, text='Sr.No', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = Label(my_w, width=15, text='Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = Label(my_w, width=15, text='Form Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = Label(my_w, width=15, text='Form Status', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = Label(my_w, width=15, text='Apply Date', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    my_w.mainloop()

def document():
    import mysql.connector
    my_w = Toplevel(root)
    my_w.geometry("450x250")
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="csc"
    )
    my_conn = my_connect.cursor()
    ####### end of connection ####
    my_conn.execute("SELECT * FROM document limit 0,100")
    i = 0
    for document in my_conn:
        for j in range(len(document)):
            e = Entry(my_w, width=15, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, document[j])
        i = i + 1
    # e = Label(my_w,width=50, text=form[j],
    #               borderwidth=2,relief='ridge', anchor="w")
    e = Label(my_w, width=15, text='Sr.No', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = Label(my_w, width=15, text='Folder Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = Label(my_w, width=15, text='Folder Location', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = Label(my_w, width=15, text='System Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    # e = Label(my_w, width=15, text='Application Number', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    # e.grid(row=0, column=4)
    # e = Label(my_w, width=15, text='Status', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    # e.grid(row=0, column=5)
    # e = Label(my_w, width=15, text='Date', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    # e.grid(row=0, column=6)
    my_w.mainloop()

def haryana():
    import mysql.connector
    my_w = Toplevel(root)
    my_w.geometry("800x250")
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="csc"
    )
    my_conn = my_connect.cursor()
    ####### end of connection ####
    my_conn.execute("SELECT * FROM haryana limit 0,100")
    i = 0
    for haryana in my_conn:
        for j in range(len(haryana)):
            e = Entry(my_w, width=15, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, haryana[j])
        i = i + 1
    # e = Label(my_w,width=50, text=form[j],
    #               borderwidth=2,relief='ridge', anchor="w")
    e = Label(my_w, width=15, text='Sr.No', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = Label(my_w, width=15, text='Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = Label(my_w, width=15, text='Father/Hus Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = Label(my_w, width=15, text='Service Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = Label(my_w, width=15, text='Application Number', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    e = Label(my_w, width=15, text='Date', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=5)
    e = Label(my_w, width=15, text='Status', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=6)
    my_w.mainloop()
def paymentdata():
    # def document():
        import mysql.connector
        my_w = Toplevel(root)
        my_w.geometry("565x250")
        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="csc"
        )
        my_conn = my_connect.cursor()
        ####### end of connection ####
        my_conn.execute("SELECT * FROM payment limit 0,10")
        i = 0
        for payment in my_conn:
            for j in range(len(payment)):
                e = Entry(my_w, width=15, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, payment[j])
            i = i + 1
        # e = Label(my_w,width=50, text=form[j],
        #               borderwidth=2,relief='ridge', anchor="w")
        e = Label(my_w, width=15, text='Sr.No', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=0)
        e = Label(my_w, width=15, text='Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=1)
        e = Label(my_w, width=15, text='Total Payment', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=2)
        e = Label(my_w, width=15, text='Deposit', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=3)
        e = Label(my_w, width=15, text='Pending', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=4)
        # e = Label(my_w, width=15, text='Status', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        # e.grid(row=0, column=5)
        # e = Label(my_w, width=15, text='Date', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        # e.grid(row=0, column=6)
        my_w.mainloop()
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
# m1.add_command(label="Record")
m1.add_command(label="Save")
mainmenu.add_cascade(label="File", menu=m1)
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Welcome")
m2.add_command(label="Feedback")
m3 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Saral Haryana", menu=m3)
m3.add_command(label="Submit Data")
mainmenu.add_cascade(label="Help", menu=m2)
submenu = Menu(mainmenu, tearoff=0)
m1.add_separator()
m1.add_cascade(label="Record", menu=submenu)
m1.add_separator()
# submenu.add_separator()
submenu.add_command(label="Saral Haryana Data", command=haryana)
submenu.add_separator()
submenu.add_command(label="Payment Record", command=paymentdata)
submenu.add_separator()
submenu.add_command(label="Form Data", command=show)
submenu.add_separator()
submenu.add_command(label="Document Record", command=document)
m1.add_command(label="Exit", command=root.destroy)
root.config(menu=mainmenu)
l1 = Label(f2, text="DIGITAL SEWA KENDRA, PUR", fg="white", bg="RED", font="comicsansms 20 bold")
l1.pack(pady=5, padx=5)
l2 = Label(f4, text="Cont:- Bintu Jangra: 9992518092, Sahil Jangra: 9306538685", fg="red", font="comicsansms 13 bold",
           padx=5)
l2.pack(side=BOTTOM, anchor="sw")

mainloop()
