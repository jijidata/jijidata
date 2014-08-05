import os
my_dir = str(input("请输入您想检测的文件路径："))

def get_size(abs_dir):
    size = os.path.getsize(abs_dir)
    return size
    
def sum_extension(my_extension):
    extension_list = []
    num_list = []
    for i in my_extension:
        if i not in extension_list:
            extension_list.append(i)
        else:
            None
    
    for x in extension_list:
        p=my_extension.count(x)
        num_list.append(p)

    for num in range(1,len(extension_list)):
        print("【%s】目录下共有类型为【%s】%d个"%(my_dir,extension_list[num],num_list[num]))        
            
    

def check_file(my_dir):
    my_file = os.listdir(my_dir)
    count_file = 0
    count_dir = 0
    my_extension = []
    for file in my_file:
        abs_path = my_dir+"\\"+file
        is_dir=os.path.isdir(abs_path)
        print("【%s】目录下\b%s\b文件的大小为\b[%.4f]\b兆" %(my_dir,os.path.basename(abs_path),get_size(abs_path)/1024/1024))
        if is_dir is True:
            count_dir+=1
        else:
            (name,extension) = os.path.splitext(file)
            my_extension.append(extension)
            count_file+=1
    print("\n")
    print("【%s】目录下共有文件夹%d个" %(my_dir,count_dir))
    sum_extension(my_extension)



            
        

check_file(my_dir)
        

