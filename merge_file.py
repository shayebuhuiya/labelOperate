import os
import shutil

label_path = r"D:\sawBlade\data2\labels"
image_path = r"D:\sawBlade\data2\images"

def changeDir(src, dst, cnt):
    filenames = os.listdir(src)
    for filename in filenames:
        path = os.path.join(src, filename)
        name1, name2 = filename.split('.')[0], filename.split('.')[1]
        saveName = str(int(name1) + cnt * 1000) + '.' + name2
        savepath = os.path.join(dst, saveName)
        shutil.copy(path, savepath)

def index(path):
    cnt = 1
    filenames = os.listdir(path)
    for filename in filenames:
        srcpath = os.path.join(path, filename)
        name1, name2 = filename.split('.')[0], filename.split('.')[1]
        savename = f"{cnt:03d}.{name2}"
        savepath = os.path.join(path, savename)
        os.rename(srcpath, savepath)
        cnt += 1


if __name__ == '__main__':
    # p = label_path
    # all = os.listdir(p)
    # cnt = 1
    # for file in all:
    #     filepath = os.path.join(p, file)
    #     changeDir(filepath, p, cnt)
    #     cnt += 1
    index(label_path)
    index(image_path)
