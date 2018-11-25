from tkinter import *
from neededFunction import *
import socket
import threading
li=[]
li2=[]
def pick():
    xuanren()


def check():
    server1=socket.socket()
    server1.bind(("127.0.0.1",5555))   #localhost
    server1.listen(20)
    while True:
        s,addr=server1.accept()
        li2.append(s)

def check1():
    for sss in li2:
        sss.send("收作业".encode("utf8"))

def kaishikaoshi():
    for sss in li2:
        sss.send("start".encode("utf8"))

def putin():
    fileupload()
def teaview():
    teawin=Tk()
    teawin.title("教师系统")
    teawin.geometry("500x380")

    aa = Canvas(teawin, width=500, height=400, )
    aa.place(x=0, y=0)
    img = PhotoImage(file=r"D:\文件处理\3.gif")
    aa.create_image(0, 0, anchor=NW, image=img)
    aa.create_text(250, 50, text="欢迎进入教师端管理系统", font=("楷体", 30))

    Inbut=Button(teawin,bg="white",text="导入题目",command=putin)
    Inbut.place(x=80,width=100,y=150,height=40)
    checkbut=Button(teawin,bg="white",text="收作业",command=check1)
    checkbut.place(x=80,width=100,y=200,height=40)
    pickbut=Button(teawin,bg="white",text="随机点名",command=pick)
    pickbut.place(x=80,width=100,y=250,height=40)
    selectbut=Button(teawin,bg="white",text="开始考试",command=kaishikaoshi)
    selectbut.place(y=300,height=40,x=80,width=100)
    teawin.mainloop()
def teaServer():
    ser = socket.socket()
    ser.bind(('127.0.0.1', 7777))
    ser.listen(20)
    while True:
        s, add = ser.accept()
        li.append(s)
        info1=s.recv(1024).decode("utf8")
        print(info1)
        if info1!="":
            stuid=info1.split("-*")[0]
            info2=info1.split("-*")[1]
            file=open(r"D:\接收文件\\"+stuid+".txt","w+")
            file.write(info2)
            file.close()
            messagebox.showinfo("提示",stuid+"的作业已上传,请在D:\接收文件\目录下查看")

def startThread():
        threading.Thread(target=teaview).start()
        threading.Thread(target=teaServer).start()
        threading.Thread(target=check).start()

