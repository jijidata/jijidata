print('''
|---  欢迎进入通讯录程序  ---|
|---  1：查询联系人资料   ---|
|---  2：插入新的联系人   ---|
|---  3：删除已有联系人   ---|
|---  4：退出通讯录程序   ---|
''')

address_list = {}

def check(n):
    if n in address_list:
        return True
    else:
        return False

def check_input(n):
    N = str(n)
    P = 1
    while P :
        try:
            command = input(N)
            P = 0
        except (KeyboardInterrupt , EOFError):
            print("退出通讯录程序必须在主菜单输入数字4才能退出哦~")
    return command

def command():
    while True:
        command = str(check_input("请输入相关的指令代码："))
        if command == "4":
            print("|---  感谢使用通录程序   ---|")
            break
        
        elif command == "1":
            Name = str(check_input("请输入联系人姓名："))
            if check(Name) :
                print("%s : %s" %(Name,address_list[Name]),"\n")
            else:
                print("此通讯录无此人电话号码，请检查后重新输入！\n")
                
        elif command == "2" :
            Name = str(check_input("请输入联系人姓名："))
            if check(Name):
                print("您输入的姓名在通讯录中已存在 --> %s : %s" %(Name,address_list[Name]))
                rewrite=str(check_input("是否修改用户资料(YES/NO)："))
                P = 1
                while P:
                    if rewrite=="NO":
                        break
                    elif rewrite == "YES":
                        phone_num = str(check_input("请输入用户联系电话："))
                        address_list[Name] = phone_num
                        P = 0
                    else :
                        print("请正确输入(YES/NO)")
                        rewrite=str(check_input("是否修改用户资料(YES/NO)："))
                else:
                    print("修改成功哦~")
                    print("\n")
            else :
                phone_num = str(check_input("请输入用户联系电话："))
                print("插入成功哦~")
                print("\n")
                address_list[Name] = phone_num

        elif command == "3":
            delname = str(check_input("请输入要删除的联系人姓名："))
            if check(delname):
                del address_list[delname]
                print("已经删除此联系人！\n")
            else:
                print("联系人里无您所要删除的人员，请检查后重新选择功能指令!\n")

        else:
            print("功能选择错误，请重新选择!\n")
            
command()
