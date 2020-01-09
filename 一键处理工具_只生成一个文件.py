# coding:utf-8
from pypinyin import lazy_pinyin, Style
from zhon.hanzi import punctuation as zp # 中文标点符号
from string import printable # 阿拉伯数字，英文字母，英文标点符号，占位符
from string import ascii_letters, punctuation, whitespace
import re
import os

li = []  # 数据集列表


def load_data(filepath):
    # 遍历filepath下所有文件，包括子目录，路径的最后要加斜杆
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi+'/')
        if os.path.isdir(fi_d):
            load_data(fi_d)
        else:
            li.append(fi_d[:-1])
    return li


def remove_symbols():
    file1 = open(file_path, 'r', encoding='utf-8')
    file2 = open(c, 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            # a_num = digits
            # b_num = '零一二三四五六七八九'
            # tran_sum = str.maketrans(a_num, b_num)

            del_estr = zp + punctuation + whitespace
            replace = "\n" * len(del_estr)
            tran_tab = str.maketrans(del_estr, replace)

            line = line.replace(' ', '')  # 去除空格及以下符号，不换行，符号之间的内容不变
            line = line.replace('“', '')
            line = line.replace('”', '')
            line = line.replace('「', '')
            line = line.replace('」', '')
            line = line.replace('《', '')
            line = line.replace('》', '')
            line = line.replace('<', '')
            line = line.replace('>', '')
            line = line.replace("'", '')
            line = line.replace('"', '')
            line = line.replace('“', '')
            line = line.replace('”', '')
            line = line.replace('‘', '')
            line = line.replace('’', '')
            line = line.replace('·', '')

            line = re.sub(u"\\(.*?\\)|\\（.*?\\）|\\{.*?}|\\[.*?]", "", line)  # 将三种括号以及里面的内容一起删除，不换行

            # line = line.translate(tran_sum)
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
            my_re = re.compile(r'[0-9A-Za-z]', re.S)
            res = re.findall(my_re, line)
            if len(line) >= 3 and not len(res): # 控制每一行有两个或以上的汉字
                file2.write(line)
            # if line == '\n': # 去空行
            #     line = line.strip("\n")
            # file2.write(line)
    finally:
        file1.close()
        file2.close()


def word_to_pinyin():
    file1 = open(b, 'r', encoding='utf-8')
    file2 = open(c, 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            line_new = " ".join(lazy_pinyin(line, style=Style.TONE)).replace('\n', '').strip()
            line_new = line_new + '\t' + line  # 拼音加汉字
            file2.write(line_new)
    finally:
        file1.close()
        file2.close()
        print(c)
        os.remove(b)


load_data('D:/语料识别/语料库/baikeqa2019+new2016zh/')  # 路径--------------------------------------------------
print(len(li))

for i in list(range(0, len(li))):
    file_path = li[i]
    (filepath, tempfilename) = os.path.split(file_path)
    (filename, extension) = os.path.splitext(tempfilename)

    b = filepath + '/' + filename + '_汉字.txt'
    c = filepath + '/' + filename + '_.txt'

    # fenhang()
    remove_symbols()
    clear_blank_line()
    word_to_pinyin()
    os.remove(li[i])
