# 这个文件的主要目的是将文件分成训练集、验证集、测试集
# 只需要改最下面的路径就行

import os
import shutil
import random
from tqdm import tqdm


def split_img(img_path, label_path, split_list):
    train_img_dir = './data/images/train'
    val_img_dir = './data/images/val'
    test_img_dir = './data/images/test'

    train_label_dir = './data/labels/train'
    val_label_dir = './data/labels/val'
    test_label_dir = './data/labels/test'

    try:
        # 创建文件夹
        os.makedirs(train_img_dir)
        os.makedirs(train_label_dir)
        os.makedirs(val_img_dir)
        os.makedirs(val_label_dir)
        os.makedirs(test_img_dir)
        os.makedirs(test_label_dir)
    except Exception as e:
        print(e)
        
    train, val, test = split_list
    all_img = os.listdir(img_path)
    all_img_path = [os.path.join(img_path, img) for img in all_img]

    train_img = random.sample(all_img_path, int(train * len(all_img_path)))
    train_label = [toLabelPath(img, label_path) for img in train_img]
    for i in tqdm(range(len(train_img)), desc='train ', ncols=80, unit='img'):
        shutil.copy(train_img[i], train_img_dir)
        shutil.copy(train_label[i], train_label_dir)
        all_img_path.remove(train_img[i])

    val_img = random.sample(all_img_path, int(val / (val + test) * len(all_img_path)))
    val_label = [toLabelPath(img, label_path) for img in val_img]
    for i in tqdm(range(len(val_img)), desc='val ', ncols=80, unit='img'):
        shutil.copy(val_img[i], val_img_dir)
        shutil.copy(val_label[i], val_label_dir)
        all_img_path.remove(val_img[i])

    test_img = all_img_path
    test_label = [toLabelPath(img, label_path) for img in test_img]
    for i in tqdm(range(len(test_img)), desc='test ', ncols=80, unit='img'):
        shutil.copy(test_img[i], test_img_dir)
        shutil.copy(test_label[i], test_label_dir)


def toLabelPath(img_path, label_path):
    img_name = os.path.basename(img_path)
    img_type = img_name.split('.')[-1]
    label = img_name.strip(img_type) + 'txt'
    return os.path.join(label_path, label)


if __name__ == '__main__':
    # 请在这里设置文件夹路径
    img_path = r'D:\sawBlade\data2\images'
    label_path = r'D:\sawBlade\data2\labels_else'
    split_list = [0.9, 0.1, 0]  # 数据集划分比例[train:val:test]
    # 将划分的数据集放到图片的上一级目录下的data文件夹下
    os.chdir(os.path.dirname(img_path))
    split_img(img_path, label_path, split_list)
