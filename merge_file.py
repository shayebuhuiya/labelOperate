import os
import shutil

org = [r"E:\sawBlade\1",
       r"E:\sawBlade\2",
       r"E:\sawBlade\3",
       r"E:\sawBlade\4"]


dst = r"E:\sawBlade\second\images"


if __name__ == '__main__':
    for path in org:
        filenames = os.listdir(path)
        for filename in filenames:
            fullPath = os.path.join(path, filename)
            dstPath = os.path.join(dst, filename)
            shutil.copy(fullPath, dstPath)
            print(dstPath)
