# encoding:utf-8
import os

def get_files(root_path):
    dir_list = os.listdir(root_path) #指定目录下所有文件名(包含文件夹名)
    for dir in dir_list:
        filenames = os.path.join(root_path, dir)   #拼接成路径
        if os.path.isdir(filenames):  #如果路径是文件夹则自循环遍历，直至非文件夹
            get_files(filenames)
        else:
            files.append(filenames)


def rename(): # 遍历所有文件名并重命名
    print('正在进行文件重命名...')
    for filename in files:
        os.rename(filename, filename + '.bak')


if __name__ == "__main__":
    files =[]  # 存放所有文件的路径
    root_path = input("请输入路径: ")

    get_files(root_path)
    rename()
    print('所有操作均完成！')