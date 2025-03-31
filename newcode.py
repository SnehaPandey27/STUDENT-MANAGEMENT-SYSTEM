from datetime import datetime


def addstudent():
    def submitadd():
        id =idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime('%H:%M:%S')
        addeddate = time.strftime('%D')
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,datetime))
            ((dob,addedtime,addeddate))
            con.commit()
            res = messagebox.askyesnocancel('notifications','Id {} Name {} Added successfully... and want to clean the form'.format(id,name),parent=addroot)
            if res == True:
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')

        except:
            messagebox.showerror('notification','Id already Exist try another id....',parent=addroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x480+117+135')
    addroot.title('student management system')
    addroot.config(bg='blue')
    addroot.iconbitmap('mana.ico')
    addroot.resizable(False,False)
    #-------------------------------------------------add student label
    idLabel = Label(addroot,text='Enter Id',bg='yellow',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idLabel.place(x=10,y=10)
    nameLabel = Label(addroot, text='Enter Name', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    nameLabel.place(x=10, y=70)
    mobileLabel = Label(addroot, text='Enter mobile', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    mobileLabel.place(x=10, y=130)
    emailLabel = Label(addroot, text='Enter Email', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    emailLabel.place(x=10, y=190)
    addressLabel = Label(addroot, text='Enter Address', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    addressLabel.place(x=10, y=250)
    genderLabel = Label(addroot, text='Enter Gender', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    genderLabel.place(x=10, y=310)
    dobLabel = Label(addroot, text='Enter D.O.B', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    dobLabel.place(x=10, y=370)

    #===================================================add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot, font=('roman',15,'bold'), bd=5, textvariable=idval)
    identry.place(x=250,y=10)
    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)
    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)
    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)
    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)
    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)
    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)
    submitbtn = Button(addroot, text='submit', font=('roman',15, 'bold'),width=20, bd=5, activebackground='blue', fg='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)

    addroot.mainloop()
    #==================================================add search details
def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime('%D')
        if id != '' :
            strr = 'select * from studentdata where id = %s'
            mycursor.execute(strr, id)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif name != '':
            strr = 'select * from studentdata where name = %s'
            mycursor.execute(strr, name)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif mobile != '':
            strr = 'select * from studentdata where mobile = %s'
            mycursor.execute(strr, mobile)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif email != '':
            strr = 'select * from studentdata where email = %s'
            mycursor.execute(strr, email)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif address != '':
            strr = 'select * from studentdata where address = %s'
            mycursor.execute(strr, address)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif gender != '':
            strr = 'select * from studentdata where gender = %s'
            mycursor.execute(strr, gender)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif dob != '':
            strr = 'select * from studentdata where dob = %s'
            mycursor.execute(strr, dob)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif addeddate != '' :
            strr = 'select * from studentdata where addeddate = %s'
            mycursor.execute(strr, addeddate)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
    searchroot = Toplevel(master = DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+120+130')
    searchroot.title('student management system')
    searchroot.config(bg='firebrick1')
    searchroot.resizable(False,False)
    #-------------------------------------------------add student label
    idLabel = Label(searchroot,text='Enter Id',bg='yellow',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idLabel.place(x=10,y=10)
    nameLabel = Label(searchroot, text='Enter Name', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    nameLabel.place(x=10, y=70)
    mobileLabel = Label(searchroot, text='Enter mobile', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    mobileLabel.place(x=10, y=130)
    emailLabel = Label(searchroot, text='Enter Email', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    emailLabel.place(x=10, y=190)
    addressLabel = Label(searchroot, text='Enter Address', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    addressLabel.place(x=10, y=250)
    genderLabel = Label(searchroot, text='Enter Gender', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    genderLabel.place(x=10, y=310)
    dobLabel = Label(searchroot, text='Enter D.O.B', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    dobLabel.place(x=10, y=370)
    dateLabel = Label(searchroot, text='Enter Date', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    dateLabel.place(x=10, y=430)

    #===================================================add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('roman',15,'bold'), bd=5, textvariable=idval)
    identry.place(x=250,y=10)
    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)
    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)
    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)
    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)
    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)
    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)
    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)
    submitbtn = Button(searchroot, text='submit', font=('roman',15, 'bold'),width=20, bd=5, activebackground='blue', fg='white',bg='red',command=search)
    submitbtn.place(x=140,y=480)

    searchroot.mainloop()
def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where id = %s'
    mycursor.execute(strr,pp)
    con.commit()
    messagebox.showinfo('notification','Id {} deleted successfully....'.format(pp))

    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)
    #==================================================add update details
def updatestudent():
    def update():
        global vv
        id =idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata set name=%s, mobile=%s, email=%s, address=%s,gender=%s, dob=%s, date=%s, time=%s, where id=%s'
        mycursor.execute(strr,(name, mobile, email, address, gender, dob, date, time, id))
        con.commit()
        messagebox.showinfo('Notification', 'Id {} Modified successfully....'.format(id),parent=updateroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+105+105')
    updateroot.title('student management system')
    updateroot.config(bg='indigo')
    updateroot.resizable(False, False)
    # -------------------------------------------------add student label
    idLabel = Label(updateroot, text='Enter Id', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    idLabel.place(x=10, y=10)
    nameLabel = Label(updateroot, text='Enter Name', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    nameLabel.place(x=10, y=70)
    mobileLabel = Label(updateroot, text='Enter mobile', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    mobileLabel.place(x=10, y=130)
    emailLabel = Label(updateroot, text='Enter Email', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    emailLabel.place(x=10, y=190)
    addressLabel = Label(updateroot, text='Enter Address', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    addressLabel.place(x=10, y=250)
    genderLabel = Label(updateroot, text='Enter Gender', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    genderLabel.place(x=10, y=310)
    dobLabel = Label(updateroot, text='Enter D.O.B', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    dobLabel.place(x=10, y=370)
    dateLabel = Label(updateroot, text='Enter Date', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    dateLabel.place(x=10, y=430)
    timeLabel = Label(updateroot, text='Enter Time', bg='yellow', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    timeLabel.place(x=10, y=490)

    # ===================================================add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)
    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)
    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)
    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)
    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)
    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)
    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)
    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)
    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)

    submitbtn = Button(updateroot, text='submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',fg='black', bg='white', command=update)
    submitbtn.place(x=150, y=535)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if len(pp) !=0 :
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()
def showallstudent():
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id, name, mobile, email, address, gender, dob, addeddate, addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),
        gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time']
    df = pandas.DataFrame(list(zip(id, name, mobile, email, address, gender, dob, addeddate, addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification', 'student data is saved {}'.format(paths))


def exitstudent():
    print('student Exit')
    res = messagebox.askyesnocancel('notification', 'Do you want to exit?')
    if res == True:
        root.destroy()
###############################################connection of database
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostvalue.get()
        user = uservalue.get()
        password = passwordvalue.get()

        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect please try again')
            return
        try:
            strr = 'create database studentmanagement'
            mycursor.execute(strr)
            strr = 'use studentmanagement'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int,name varchar(50),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(10),dob varchar(10),date varchar(10),time varchar(10))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('notification', 'Database created and now you are connected to the database...',parent=dbroot)
        except:
            strr = 'use studentmanagement'
            mycursor.execute(strr)
            messagebox.showinfo('notification','Now you are connected to the database...',parent=dbroot)
            dbroot.destroy()
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+700+150')
    dbroot.iconbitmap('mana.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')

#--------------------------connectdb labels
    hostLabel = Label(dbroot, text="Enter Host ", bg='gold2', font=('times',20,'bold'),relief=GROOVE, borderwidth=3, width=13, anchor='w')
    hostLabel.place(x=10,y=10)

    userLabel = Label(dbroot, text="Enter User ", bg='gold2', font=('times',20,'bold'),relief=GROOVE, borderwidth=3, width=12, anchor='w')
    userLabel.place(x=10,y=70)

    passwordLabel = Label(dbroot, text="Enter Password ", bg='gold2', font=('times',20,'bold'),relief=GROOVE, borderwidth=3, width=13, anchor='w')
    passwordLabel.place(x=10,y=130)

 #---------------------------------Connectdb entry
    hostvalue = StringVar()
    uservalue = StringVar()
    passwordvalue = StringVar()
    hostentry = Entry(dbroot, font=('roman',15,'bold'),bd=5, textvariable=hostvalue)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('roman',15,'bold'),bd=5, textvariable=uservalue)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot, font=('roman',15,'bold'),bd=5, textvariable=passwordvalue)
    passwordentry.place(x=250,y=130)

    #------------------------------------connectdb button
    submitbutton = Button(dbroot, text='submit',font=('roman', 15, 'bold'),bg='red',bd=5,width=20, activebackground='blue',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()

###############################################date and time
def tick():
    time_String = time.strftime("%H:%M:%S")
    date_String = time.strftime("%D")
    clock.config(text='Date :'+date_String+"\n"+"Time : "+time_String)
    clock.after(200,tick)
########################################## intro slider
import random
colors = ['red','green','blue','yellow','pink','red2','gold2']
def IntroLabelcolorTick():
    fg =random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelcolorTick)
def IntroLabelTick():
    global count, text
    if count >= len(ss):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, IntroLabelTick)
###########################importing part
from tkinter import*
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title('student management system')
root.config(bg='gold2')
root.geometry('1174x700+105+20')
root.iconbitmap('mana.ico')
root.resizable(False, False)
############################################### frames
####################################################dataentry frame
DataEntryFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=600)
FrontLabel = Label(DataEntryFrame,text='-----------welcome-------------', width=30, font=('arial', 22, 'italic bold'),bg='gold2')
FrontLabel.pack(side=TOP,expand=True)
addbtn=Button(DataEntryFrame, text='Add student', width=25, font=('times', 20, 'bold'),bd=6,bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=addstudent)
addbtn.pack(side=TOP, expand=True)

searchbtn=Button(DataEntryFrame, text='Search student', width=25, font=('times', 20, 'bold'),bd=6,bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP, expand=True)

deletebtn=Button(DataEntryFrame, text='Delete student', width=25, font=('times', 20, 'bold'),bd=6,bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP, expand=True)

updatebtn=Button(DataEntryFrame, text='Update student', width=25, font=('times', 20, 'bold'),bd=6,bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP, expand=True)

showallbtn=Button(DataEntryFrame, text='Show all', width=25, font=('times', 20, 'bold'),bd=6,bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white',command=showallstudent)
showallbtn.pack(side=TOP, expand=True)

exportbtn=Button(DataEntryFrame, text='Export data', width=25, font=('times', 20, 'bold'),bd=6,bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP, expand=True)

exitbtn=Button(DataEntryFrame, text=' Exit', width=25, font=('times', 20, 'bold'),bd=6,bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP, expand=True)







#---------------------------------------show data frame
ShowDataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=500, y=80, width=620, height=600)
#==============================================showdataframe
style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview.Heading',font=('times',15,'bold'),background='cyan',foreground='black')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttable = Treeview(ShowDataFrame, columns=('Id','Name','Mobile No.', 'Branch', 'Email', 'Address','Gender', 'D.O.B', 'Added Date', 'Added Time'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('Branch',text='Branch')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id', width=100)
studenttable.column('Name', width=300)
studenttable.column('Mobile No.', width=200)
studenttable.column('Branch', width=300)
studenttable.column('Email', width=300)
studenttable.column('Address', width=400)
studenttable.column('Gender', width=100)
studenttable.column('D.O.B', width=200)
studenttable.column('Added Date', width=200)
studenttable.column('Added Time', width=200)


studenttable.pack(fill=BOTH, expand=1)

################################################ slider
ss = 'Welcome To Student Management System'
count = 0
text = ''
#################################################
SliderLabel = Label(root, text=ss, font=('chiller',30,'italic bold'), relief=RIDGE, borderwidth=5, width=35, bg='cyan')
SliderLabel.place(x=260, y=0)
IntroLabelTick()
IntroLabelcolorTick()
################################################### clock
clock = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=4, bg='magenta')
clock.place(x=0, y=0)
tick()
###################################################### connect to database button
connectbutton = Button(root, text='Connect To Database', width=23, font=('chiller',19,'italic bold'), relief=RIDGE, bd=6, borderwidth=5, bg='red'
                       , activebackground='blue', activeforeground='white', command=Connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()