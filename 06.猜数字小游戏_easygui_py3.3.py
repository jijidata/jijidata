import random
import easygui as g
import os

entergui = g.enterbox(msg = "不妨猜一下小甲鱼现在心里想的是哪个数字：",title = "猜数字小游戏")

secret = random.randint(1,10)

temp = entergui

try:
    guess = int(temp)
except ValueError :
    guess = float(temp)

while guess != secret:
    temp = g.enterbox(msg = "哎呀，猜错了，请重新输入吧~：",title = "猜数字小游戏")
    try:
        guess = int(temp)
    except ValueError:
        guess = float(temp)
        
    if guess == secret:
        g.msgbox(msg = "我草，你是小甲鱼心里的蛔虫吗？！",ok_button="点我")
        g.msgbox(msg = "哼，猜中了也没有奖励哦~",ok_button="嘿嘿~")
    else:
        if guess > secret:
            g.msgbox(msg = "哥，大了大了~~~",ok_button="重新猜")
        else:
            g.msgbox(msg = "嘿，小了，小了~~~",ok_button="重新猜")
g.msgbox(msg = "游戏结束，不玩啦^_^",ok_button="拜拜")

