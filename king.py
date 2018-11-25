import pymysql
from tkinter import *
import tkinter.messagebox
class  froms():
    def check(cur,var1,i,count,m,list1,list2):
        sql11="select ios from timu2"
        row=cur.execute(sql11)
        if row==count:
            var1.set("题目已经做完了")
            tkinter.messagebox.showerror("错误","题目已经出完了")
            return
        else:
            sql="select * from timu2  order  by rand() limit %s"#随机 出题
            cur.execute(sql,(i))
            add=cur.fetchone()

            if add[2] not in list2:
                list2.append(add[2])
                list1.append(add[1])
                m+=1
                var1.set(add[2]+"\n"+add[3]+"\n"+add[4]+"\n"+add[5]+"\n"+add[6])
                count+=1
                i+=1
            else:
                froms.check(cur,var1,i,count,m,list1,list2)
            return i,m,count,list1
    def get(var2,var3):
        commm=var3.get()
        var2.set("您的选择是："+commm)
    def xxx(var3,m,list1,var2,cur,coon,stuid):
        cnnn=var3.get()
        if str(cnnn)==list1[m-1]:
            var2.set("回答正确")
            sql12="update mark set mark=mark+20 WHERE id=%s"
            cur.execute(sql12,(stuid))
            coon.commit()
        else:
            var2.set("回答错误")
    def big(self,cur,stuid):
        sql13 = "select mark from mark WHERE id=%s"
        cur.execute(sql13, (stuid))
    def exit(fd):
        fd.exit()
    def orang(var2,cur,stuid):
        sql2 = "select mark from mark WHERE id=%s"
        cur.execute(sql2,(stuid))
        ond=cur.fetchone()[0]
        var2.set("您的得分是："+str(ond))

    def come(self,stuid):
        list1 = []
        list2 = []
        i = 1
        m = 0
        count = 0
        fd = Toplevel()
        fd.title("考试系统")
        fd.geometry("900x900")
        coon = pymysql.connect(host="localhost", port=3306,
                               user="root", password="admin123456",
                               database="test1", charset="utf8")
        cur = coon.cursor()
        var1 = StringVar()
        var1.set("点击下一题考试")
        var2 = StringVar()
        var3 = StringVar()
        var3.set("a")
        label = Label(fd, textvariable=var1, bg="#44ffff", font=("Arial", 12))
        label.place(x=0, y=0, height=300, width=700)
        label = Label(fd, textvariable=var2, bg="red", font=("Arial", 12))
        label.place(x=700, y=0, height=300, width=200)
        button1 = Radiobutton(fd, text="A", value="A", variable=var3, bg="white",
                                      command=lambda: froms.get(var2, var3))
        button1.place(x=400, y=400, height=30, width=100)
        button2 = Radiobutton(fd, text="B", value="B", variable=var3, bg="white",
                                      command=lambda: froms.get(var2, var3))
        button2.place(x=400, y=450, height=30, width=100)
        button3 = Radiobutton(fd, text="C", value="C", variable=var3, bg="white",
                                      command=lambda: froms.get(var2, var3))
        button3.place(x=400, y=500, height=30, width=100)
        button4 = Radiobutton(fd, text="D", value="D", variable=var3, bg="white",
                                      command=lambda: froms.get(var2,var3))
        button4.place(x=400, y=550, height=30, width=100)
        button5 = Button(fd, text="下一题", bg="white", command=lambda: froms.check(cur, var1, i, count, m,list1,list2))
        button5.place(x=0, y=330, height=60, width=150)  # 随机选题
        button6 = Button(fd, text="判断对错", bg="white", command=lambda: froms.xxx(var3,m, list1, var2,cur,coon,stuid))
        button6.place(x=0, y=420, height=60, width=150)
        button7 = Button(fd, text="查询成绩", bg="white", command=lambda :froms.orang(var2,cur,stuid))
        button7.place(x=0, y=510, height=60, width=150)
        button8 = Button(fd, text="退出", bg="white", command=lambda :exit(fd))
        button8.place(x=0, y=600, height=60, width=150)
        fd.mainloop()
