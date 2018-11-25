from tkinter import *
from neededFunction import *
import socket
import threading
from king import froms

def sign(stuid):
    qiandao(stuid)

def submit(stuid):
    jiaozuoye(stuid)

def zaixianzice():
    selfexam()

def chaxunchengji(stuid):
    querry(stuid)

def kaishikaoshi(stuid,f):

    f.come(stuid)

def resetScore(stuid):
    reset(stuid)

def stuview(stuid,stuname):
    stuwin=Tk()
    stuwin.title(stuname)
    stuwin.geometry("500x380")

    aa = Canvas(stuwin, width=500, height=400, )
    aa.place(x=0, y=0)
    img = PhotoImage(file=r"D:\文件处理\2.gif")
    aa.create_image(0, 0, anchor=NW, image=img)
    aa.create_text(250, 50, text="欢迎进入学生端考试系统", font=("楷体", 30))



    Inbut=Button(stuwin,bg="white",text="学生签到",command=lambda: sign(stuid))
    Inbut.place(x=80,width=100,y=150,height=40)
    checkbut=Button(stuwin,bg="white",text="在线自测",command=zaixianzice)
    checkbut.place(x=80,width=100,y=200,height=40)
    pickbut=Button(stuwin,bg="white",text="查询成绩",command=lambda :chaxunchengji(stuid))
    pickbut.place(x=80,width=100,y=250,height=40)
    selectbut=Button(stuwin,bg="white",text="上交作业",command=lambda :submit(stuid))
    selectbut.place(y=300,height=40,x=80,width=100)
    stuwin.mainloop()
def startServer(stuid,f):
    try:
        server = socket.socket()
        server.connect(('127.0.0.1', 5555))
        while True:
            info=server.recv(1024).decode("utf8")
            if info=="start":
                messagebox.showinfo("提示","老师已下发试卷,请开始答题")
                # resetScore(stuid)
                kaishikaoshi(stuid,f)

            else:
                messagebox.showinfo("",info)
    except:""

def Start(stuid,stuname):
    f = froms()
    threading.Thread(target=stuview,args=(stuid,stuname)).start()
    threading.Thread(target=startServer,args=(stuid,f)).start()



