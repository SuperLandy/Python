# encoding:utf-8
import os
import zipfile


def zip_file(base_dir, filename):

    output_filename = base_dir + filename  # 压缩后文件夹的名字
    f = zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED)  #初始化f

    for root_path, dirs, file_names in os.walk(base_dir):
        f_path = root_path.replace(base_dir, '') + os.sep or ''  # 相当于把base_dir作基本路径
        # f_path = fpath and fpath + os.sep or ''
        for fn in file_names:
            if fn == filename:
                pass
            else:
                f.write(os.path.join(root_path, fn), f_path + fn)
    f.close()   

if __name__ == "__main__":
    zip_file(r'd:/test/' , 'sun.zip')