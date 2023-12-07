# 这个文件主要目的有
# 1. 类型检查，检查是否在给定类别内
# 2. 将xml文件转换成txt文件

import xml.etree.ElementTree as ET
import os

# 类别
classes = ['left_unqualified', 'left_qualified', 'right_unqualified', 'right_qualified', 'incomplete']
xml_path = r"D:\sawBlade\data2\labels"


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(filepath):
    in_file = open(filepath, encoding='UTF-8')
    image_id = os.path.basename(filepath).strip('.xml')
    out_file = open(r'./labels_else\%s.txt' % image_id, 'w')  # 生成txt格式文件
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        # print(cls)
        if cls not in classes:
            print(cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == '__main__':
    # 标签检查
    filenames = os.listdir(xml_path)
    paths = [os.path.join(xml_path, filename) for filename in filenames]
    for file in paths:
        tree = ET.parse(file)
        root = tree.getroot()
        name = root.find(".//name")
        if name is not None and classes.count(name.text) == 0:
            print(f"{file}: {name}")

    # 转类型
    _dir = os.path.dirname(xml_path)
    os.chdir(_dir)
    txt_path = './labels_else'
    try:
        os.makedirs(txt_path)
    except Exception as e:
        print(e)

    label_xmls = os.listdir(xml_path)
    for label_xml in label_xmls:
        filepath = os.path.join(xml_path, label_xml)
        print(filepath)
        convert_annotation(filepath)
