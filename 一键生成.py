# coding:utf-8
# 一键去标点、去空行、转拼音等操作，生成一份汉字文件和拼音文件

from pypinyin import lazy_pinyin, Style
from zhon.hanzi import punctuation as zp # 中文标点符号
from string import printable # 阿拉伯数字，英文字母，英文标点符号，占位符
from string import digits # 阿拉伯数字
import os

file_path = "../数据集/wiki_00"
(filepath, tempfilename) = os.path.split(file_path)
(filename, extension) = os.path.splitext(tempfilename)

# print((filepath, tempfilename))
# print((filename, extension))
# a = ''
# d = a.split('.')[0]

b = filepath + '/' + filename + '_汉字.txt'
c = filepath + '/' + filename + '_拼音.txt'


# def fenhang(): # file2是保存偶数行的文件，file3是奇数行
#     file1 = open(a, 'r', encoding='utf-8')
#     file2 = open(b, 'w', encoding='utf-8')
#     # file3 = open(c, 'w', encoding='utf-8')
#     lines = file1.readlines()
#     i = 0
#     for line in lines:
#         i += 1
#         if i % 2 == 0:
#             file2.write(line)
#         # else:
#         #     file3.write(line)
#     file1.close()
#     file2.close()
#     # file3.close()


def remove_symbols():
    file1 = open(file_path, 'r', encoding='utf-8')
    file2 = open(c, 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            a_num = digits
            b_num = '零一二三四五六七八九'
            tran_sum = str.maketrans(a_num, b_num)

            del_estr = zp + printable
            replace = "\n" * len(del_estr)
            tran_tab = str.maketrans(del_estr, replace)

            line = line.replace(' ', '') # 去除空格
            line = line.translate(tran_sum)
            line = line.translate(tran_tab)

            file2.writelines(line)
    finally:
        file1.close()
        file2.close()


def clear_blank_line():
    file1 = open(c, 'r', encoding='utf-8')
    file2 = open(b, 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            # if len(line) >= 5: # 控制每一行有四个或以上的汉字
            #     file2.write(line)
            if line == '\n': # 去空行
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


def word_to_pinyin():
    file1 = open(b, 'r', encoding='utf-8')
    file2 = open(c, 'w+', encoding='utf-8')
    try:
        for line in file1.readlines():
            line = " ".join(lazy_pinyin(line, style=Style.TONE))
            file2.write(line)
    finally:
        file1.close()
        file2.close()


# fenhang()
remove_symbols()
clear_blank_line()
word_to_pinyin()
