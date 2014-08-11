from random import *


def checkpos(n): #保证移动范围在0~10之间
    if 0 <= n <= 10:
        return n
    else :
        p = n//10
        s = n-(p*10)
        return s

    
    
class Cuckold :
    def __init__(self):
        self.pos_startX = randint(0,10)
        self.pos_startY = randint(0,10)
        self.HP = 100
        
    

    def move(self):
        step = randint(1,2)
        self.HP -=step
        if step == 1:
            XandY = choice(["X","Y"])
            if XandY == "X":
                self.pos_startX = self.pos_startX + choice([-1,1])
                POS = [checkpos(self.pos_startX),checkpos(self.pos_startY)]
                return POS
            else:
                self.pos_startY = self.pos_startY + choice([-1,1])
                POS = [checkpos(self.pos_startX),checkpos(self.pos_startY)]
                return POS
        else:
            XandY = choice(["X","Y","XandY","YandX"])
            if XandY == "X":
                self.pos_startX = self.pos_startX + choice([-2,2])
                POS = [checkpos(self.pos_startX),checkpos(self.pos_startY)]
                return POS
            elif XandY == "Y":
                self.pos_startY = self.pos_startY + choice([-2,2])
                POS = [checkpos(self.pos_startX),checkpos(self.pos_startY)]
                return POS
            elif XandY == "XandY" :
                self.pos_startX = self.pos_startX + choice([-1,1])
                self.pos_startY = self.pos_startY + choice([-1,1])
                POS = [checkpos(self.pos_startX),checkpos(self.pos_startY)]
                return POS
            else:
                self.pos_startX = self.pos_startX + choice([-1,1])
                self.pos_startY = self.pos_startY + choice([-1,1])
                POS = [checkpos(self.pos_startX),checkpos(self.pos_startY)]
                return POS

    def eat(self):
        self.HP+= 20
        if self.HP >= 100:
            self.HP =100
            

class Fish:
    def __init__(self) :
        self.pos_startX = randint(0,10)
        self.pos_startY = randint(0,10)

    def move(self):
        XandY = choice(["X","Y"])
        if XandY == "X":
            self.pos_startX = self.pos_startX + choice([-1,1])
            POS = [checkpos(self.pos_startX),checkpos(self.pos_startY)]
            return POS
        else:
            self.pos_startY = self.pos_startY + choice([-1,1])
            POS = [checkpos(self.pos_startX),checkpos(self.pos_startY)]
            return POS
        



cu = Cuckold()
fi = []
for i in range(1,11):
    f = Fish()
    fi.append(f)
    
cuckold_num = 1

    
start = 1
while start :

    if cu.HP == 0:
        print("乌龟HP为零，游戏结束！")
        start = 0
    if len(fi) ==0:
        print("鱼被吃完了，游戏结束！")
        start = 0
    cu_pos = cu.move()
    for each in fi[:]:       
        if each.move() == cu_pos :
            cu.eat()
            fi.remove(each)
            print("一条小鱼被吃掉了，还剩%d条"%len(fi))
            if (len(fi) ==0) or (cu.HP == 0) :
                break
            
            
    
        
    
    
    
    

                
                
                


                
                
        
        
