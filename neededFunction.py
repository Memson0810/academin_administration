import pymysql
from tkinter import messagebox
import socket
from tkinter import  filedialog
import time
import  tkinter
from random import *
from tkinter import *
conn = pymysql.connect(host="localhost", port=3306, user="root",
                           password="admin123456", database="test1", charset="utf8")
cur=conn.cursor()

def xuanren():
    import pymysql
    from random import choice
    import tkinter.messagebox
    list2=[]
    sql="select stuName from stuInfo"
    cur.execute(sql)
    list1=cur.fetchall()
    for i in list1:
        list2.append(i)
    aa=choice(list2)
    bb=list(aa)
    tkinter.messagebox.showinfo("恭喜",bb[0])
def stuv(stuid,stuname):
    li2=[]
    sql="select stuId,stuName from stuInfo"
    cur.execute(sql)
    stuinfo=list(cur.fetchall())
    for i in stuinfo:
        j=list(i)
        li2.append(j)
    if [stuid,stuname] in li2:
        messagebox.showinfo("提示","登录成功")
        return  1
    else:
        messagebox.showerror("错误", "学号或密码错误")
        return 2
def teav(teaid,teaname):
    li2=[]
    sql="select teaId,teaName from teaInfo"
    cur.execute(sql)
    stuinfo=list(cur.fetchall())
    for i in stuinfo:
        j=list(i)
        li2.append(j)
    if [teaid,teaname] in li2:
        messagebox.showinfo("提示","登录成功")
        return 1
    else:
        messagebox.showerror("错误","学号或密码错误")
        return 2
def qiandao(stuid):
    li=[]
    tm = time.ctime().split(":")
    tm = tm[0] + ":" + tm[1]
    ip = socket.gethostbyname(socket.gethostname())
    tmip1=tm+"---"+ip
    sql="select tmip from score where stuId=%s"
    cur.execute(sql,stuid)
    m1=cur.fetchone()
    m=m1[0]
    print(tmip1)
    print(m1)
    if tmip1==m:
        messagebox.showerror("","签到过了")
    else:
        sql2="update score set tmip = %s where stuId=%s"
        cur.execute(sql2,(tmip1,stuid))
        conn.commit()
        messagebox.showinfo("","签到成功")


    # sql="update score set performance=performance +5 where stuid=%s"
    # cur.execute(sql,(stuid,))
    # conn.commit()
    # messagebox.showinfo("恭喜","签到成功")
def fileupload():
    # 选择路径
    try:
        filename=filedialog.askopenfilename(title="请选择导入文件")
        file=open(filename,"r")
        list=file.readlines()
    except:""
        # 写入数据库
    for i in list:
        sql = "insert into timu2 values(%s,%s,%s,%s,%s,%s,%s)"
        row=cur.execute(sql,(i.split("*")[0],i.split("*")[1],i.split("*")[2],i.split("*")[3],i.split("*")[4],i.split("*")[5],i.split("*")[6]))
        conn.commit()

    messagebox.showinfo(title="恭喜",message="导入成功")
def jiaozuoye(stuid):
    server2 = socket.socket()
    server2.connect(('127.0.0.1', 7777))
    try:
        name=filedialog.askopenfilename()
        file1=open(name,"r+")
        file=file1.read(1024)
        print(file)
        file1.close()
        server2.send((str(stuid)+"-*"+file).encode("utf-8"))
    except FileNotFoundError:
        messagebox.showerror("错误","未选文件")
def format(gross):
    j=str(gross).partition("A．")
    sec1=j[0]+"\n"+j[1]+j[2]
    j=str(sec1).partition("C．")
    sec1=j[0]+"\n"+j[1]+j[2]
    j=str(sec1).partition("B．")
    sec1=j[0]+"\n"+j[1]+j[2]
    j=str(sec1).partition("D．")
    sec1=j[0]+"\n"+j[1]+j[2]

    sec1=sec1.replace("'"," ")
    sec1=sec1.replace(","," ")
    sec1=sec1.replace("("," ")
    sec1=sec1.replace(")"," ")
    return sec1
i=1
def selfexam():
    ziceapp = Toplevel()
    ziceapp.title("自测")
    ziceapp.geometry("800x600")

    var = StringVar()
    var.set("考试测试")
    var1 = StringVar()
    var1.set("答案")
    sql = "select * from timu2"
    cur.execute(sql)
    timulist = cur.fetchall()
    list2 = []
    for i in timulist:
        list2.append(i)
    aa = choice(list2)
    bb = list(aa)
    timo = bb[2] + "\n" + bb[3] + "\n" + bb[4] + "\n" + bb[5] + "\n" + bb[6]
    list3 = []
    def kaishi():
        var.set("开始测试，请点随机出题")

    def xiayita():
        global bb
        bb = choice(list2)
        timo = bb[2] + "\n" + bb[3] + "\n" + bb[4] + "\n" + bb[5] + "\n" + bb[6]
        if bb not in list3:
            var.set(timo)
            list3.append(bb)
        else:
            xiayita()

    def A():
        var1.set("A")

    def B():
        var1.set("B")

    def C():
        var1.set("C")

    def D():
        var1.set("D")

    def queren():
        global bb
        a = bb[0]
        sql = "select num from timu2 where ios=%s"
        cur.execute(sql, (a))
        num = cur.fetchone()
        danan = list(num)[0]
        shuru = var1.get()
        if danan == shuru:
            var1.set("对")
        else:
            var1.set("错")
        list3.append(a)
        return bb

    label = Label(ziceapp, bg="white", textvariable=var, font=("宋体", 20))
    label.place(x=0, y=0, width=800, height=400)

    label1 = Label(ziceapp, bg="white", textvariable=var1, font=("宋体", 20))
    label1.place(x=0, y=401, width=800, height=60)

    a = tkinter.Button(ziceapp, text="A", command=A, font=("宋体", 20), bg="#aeeeee")
    a.place(x=40, y=461, height=50, width=120)

    b = tkinter.Button(ziceapp, text="B", command=B, font=("宋体", 20), bg="#aeeeee")
    b.place(x=160, y=461, height=50, width=120)

    c = tkinter.Button(ziceapp, text="C", command=C, font=("宋体", 20), bg="#aeeeee")
    c.place(x=280, y=461, height=50, width=120)

    d = tkinter.Button(ziceapp, text="D", command=D, font=("宋体", 20), bg="#aeeeee")
    d.place(x=400, y=461, height=50, width=120)

    kaishi = tkinter.Button(ziceapp, text="开始测试", bg="#056eee", command=kaishi, font=("宋体", 20))
    kaishi.place(x=300, y=530, height=60, width=200)

    queren = tkinter.Button(ziceapp, text="确认", command=queren, font=("宋体", 20), bg="#aeeeee")
    queren.place(x=520, y=461, height=50, width=120)

    xiayiti = tkinter.Button(ziceapp, text="随机出题", command=xiayita, font=("宋体", 20), bg="#aeeeee")
    xiayiti.place(x=640, y=461, height=50, width=120)
    ziceapp.mainloop()

def querry(stuid):
    sql = "select mark from mark where id =%s"
    cur.execute(sql, stuid)
    score = cur.fetchone()
    score = format(score)
    messagebox.showinfo("成绩查询","学号为 "+stuid+" 的成绩为 "+score)

def reset(stuid):
    sql3="update mark set mark = 0 where id =%s"
    cur.execute(sql3,(stuid,))
    conn.commit()




