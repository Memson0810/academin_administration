from  studentview import  *
from teacherview import  startThread

win=Tk()
win.title("登录系统")
win.geometry("400x325")
v1=StringVar()
v2=StringVar()

def StuVerify():
    stuid=entry1.get()
    stuname=entry2.get()
    num=stuv(stuid,stuname)
    if num==1:
        win.destroy()
        Start(stuid,stuname)

def TeaVerify():
    teaid=entry1.get()
    teaname=entry2.get()
    num=teav(teaid,teaname)
    if num==1:
        win.destroy()
        startThread()

aa=Canvas(win,width=400,height=360,)
aa.place(x=0,y=0)
img = PhotoImage(file = r"D:\文件处理\1.gif")
aa.create_image(0,0,anchor=NW,image = img)
aa.create_text(220,50,text="欢迎进入教务系统",font=("楷体",30))
aa.create_text(80,120,text="账号",font=("楷体",20))
aa.create_text(80,170,text="姓名",font=("楷体",20))

entry1=Entry(win,textvariable=v1,font=("",18))
entry1.place(x=120,y=100,height=35,width=210)
entry2=Entry(win,textvariable=v2,font=("",18))
entry2.place(x=120,y=150,height=35,width=210)
but=Button(win,text="学生登录",font=("黑体",11),bg="white",command=StuVerify)
but.place(x=130,y=210,height=35,width=90)
but=Button(win,text="教师登录",font=("黑体",11),bg="white",command=TeaVerify)
but.place(x=230,y=210,height=35,width=90)
win.mainloop()