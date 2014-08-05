import os

start_dir = str(input("请输入待查找的初始目录："))
extension = str('.'+input("请输入要查找扩展名(不需要打入点号)："))
              
all_dir = []           #所有的目录
all_file = []           #所有的文件
all_name=[]         #所有文件名
all_extension=[]    #所有扩展名
find_file = []         #符合所查找的文件名.扩展名
f = open("%s\\result.txt"%start_dir, "w")


def list_all_dir(path):
    """列出所有目录以及所有目录下的文件"""
    for root,dirs,files in os.walk(path):
        all_dir.append(root)
        all_file.append(files)



def list_name_extension(all_file):
    '''列出所有文件名以及扩展名,并且两组列表内容相互对应'''
    for x in range(len(all_file)):
        for y in all_file[x]:
            (name, extension) = os.path.splitext(y)
            all_name.append(name)
            all_extension.append(extension)


def find_extension(extension):
    '''判断扩展名是否是大小写，仅适用于全是大写或全是小写，大小写混合的暂时不适用'''
    for x in range(len(all_extension)):
        if (extension == all_extension[x]) :
            filename = all_name[x]+extension
            find_file.append(filename)
        elif (extension.upper() == all_extension[x]):
            filename = all_name[x]+extension.upper()
            find_file.append(filename)


def search_file(files):
    '''遍历所有的查找目录，列出文件，若存在，打印出目录名'''
    for x in all_dir:
         if files in os.listdir(x):
            print("%s在%s目录下" %(files,x))            
            f.write("%s\\%s\n"%(x,files))
           
def search(find_file):
    '''判断是否目录下是否含有此文件，如果有，则输出，没有则告知~'''
    find_files = set(find_file)
    if len(find_files) != 0:
        for n in find_files:
            search_file(n)
    else:
        print("该目录下没有此类型的文件！")
        
list_all_dir(start_dir)

list_name_extension(all_file)
find_extension(extension)
search(find_file)
f.close()

    
    

