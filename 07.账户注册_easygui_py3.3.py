import random
import easygui as g
import os




def check(account):
    try:
        name = (account[0] is "") or (" " in account[0])
        real_name = (account[1] is "") or (" " in account[1])
        phone_num = (account[3] is "") or (" " in account[3])
        mail = (account[5] is "") or (" " in account[5])
        judge = name or real_name or phone_num or mail
        if judge is True:
            return True
        else:
            return False
    except TypeError :
        g.msgbox(msg = "要走么~拜拜~")
        

def msg():
    g.msgbox(msg = "带*号的请务必输入哦，并且不能含有空格~")

def Run():
    account = g.multenterbox(msg = "【*用户名】为必填选项\n【*真实姓名】为必填选项\n【*手机号码】为必填选项\n【*E-mail】为必填选项",title = "账号中心",fields = ("*用户名","*真实姓名","固定电话","*手机号码","QQ号码","*Email"))
    P = 1
    while P :
        if check(account) is True:
            msg()
            account = g.multenterbox(msg = "【*用户名】为必填选项\n【*真实姓名】为必填选项\n【*手机号码】为必填选项\n【*E-mail】为必填选项",title = "账号中心",fields = ("*用户名","*真实姓名","固定电话","*手机号码","QQ号码","*Email"))
        else:         
            P = 0
    else:
        return account

p =Run()

