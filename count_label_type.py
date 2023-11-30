# 这个文件用于检查文件类型是否对应
# 1. 是否在给定类别内
# 2. 是否符合文件名定义的类型

import os
import xml.etree.ElementTree as ET

path = r"E:\sawBlade\second\labels"
types = ["left_qualified", "right_qualified", "left_unqualified", "right_unqualified"]

if __name__ == "__main__":
    filenames = os.listdir(path)
    paths = [os.path.join(path, filename) for filename in filenames]
    for file in paths:
        tree = ET.parse(file)
        root = tree.getroot()
        name = root.find(".//name")
        qualified = (int(os.path.basename(file).split('.')[0]) >= 10000)
        if name is not None and types.count(name.text) == 0:
            print(f"{file}: {name}")
        if name is not None and not qualified:
            print(f"{file}: {name}")
            if name.text == types[0]:
                name.text = types[2]
            if name.text == types[1]:
                name.text = types[3]
            tree.write(file)
