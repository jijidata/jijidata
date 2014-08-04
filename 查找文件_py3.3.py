import os

start_dir = str(input("请输入待查找的初始目录："))
find_file = str(input("请输入要查找的目标文件："))



                
all_dir = []
all_file = []


def list_all_dir(path):
    """列出所有目录以及所有目录下的文件"""
    for root,dirs,files in os.walk(path):
        all_dir.append(root)
        all_file.append(files)
list_all_dir(start_dir )

def file_exist(find_file):
    '''判断所查找的目标文件是否在所有的文件中，若有一个存在，返回True，否则，返回False'''
    L = len(all_file)
    for x in range(L):
        if find_file in all_file[x]:
            A = True
            break
        else:
            A = False
    return A
        

def search_file(find_file):
    '''若file_exist函数返回True，则执行以下循环：遍历所有的查找目录，列出文件，若存在，打印出目录名'''
    if file_exist(find_file) is True:
        for x in all_dir:
            if find_file in os.listdir(x):
                print("%s在%s目录下" %(find_file,x))
    else:
        print("没有找到此文件")

search_file(find_file)

        

