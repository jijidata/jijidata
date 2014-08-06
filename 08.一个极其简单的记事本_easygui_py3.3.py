import easygui as g
import sys
import os

L = []

my_file=g.fileopenbox(msg = "请选择一个文本文件",title = "浏览文件",filetypes = [["*.txt", "文本文件"]] )
try :
    file_open =open(my_file)
    notpade = g.textbox(msg="文件内容显示如下",title="显示文件",text =file_open,codebox = 0)
except TypeError:
    None

def detect():
    try:
        origi_file = open(my_file)
        origi_file.seek(0)
        data = origi_file.read()
        if data+"\n"== notpade:
            return True
        else:
            return False
    except TypeError:
        return True
detect()

def decided():
    if detect() is False:
        done = g.buttonbox(msg = "检测到文件内容发生改变，请选择以下操作",title = "警告", choices = ("放弃保存","覆盖保存","另存为..."))
        return done
    elif detect() is True:
        g.msgbox(msg = "感谢使用~",title = "文本阅读器",ok_button="拜拜~")
do = decided()

def last_job():
    if do == "放弃保存":
        g.msgbox(msg = "感谢使用~",title = "文本阅读器",ok_button="拜拜~")
    elif do == "覆盖保存":
        try:
            now_file = open(my_file,"w")
            now_file.write(notpade)
            now_file.close()
        except TypeError:
            g.msgbox(msg = "您已取消覆盖，文件将不会改变。",title = "文本阅读器",ok_button="拜拜~")
    elif do == "另存为...":
        try:
            file_name = os.path.basename(my_file)
            p = g.filesavebox(title = "另存为",default=file_name+'_new.txt',filetypes = [["*.txt", "文本文件"]])
            other_file = open(p,"w")
            other_file.write(notpade)
            other_file.close()
        except TypeError:
            g.msgbox(msg = "您已取消另存为，文件将不会改变。",title = "文本阅读器",ok_button="拜拜~")
            
    else:
        None           
last_job()
