# python读取文件，偶数行输出一个文件，奇数行输出一个文件
import os

file_path = "../数据集/哈工大数据集/哈工大信息检索研究室汉英双语语料库_样例.txt"
(filepath, tempfilename) = os.path.split(file_path)
(filename, extension) = os.path.splitext(tempfilename)

b = filepath + '/' + filename + '_偶数行.txt'
c = filepath + '/' + filename + '_奇数行.txt'


def fenhang():
    infopen = open(file_path, 'r', encoding='utf-8')
    outopen1 = open(b, 'w', encoding='utf-8')
    outopen2 = open(c, 'w', encoding='utf-8')
    lines = infopen.readlines()
    i = 0
    for line in lines:
        i += 1
        if i % 2 == 0:
            outopen1.write(line)
        else:
            outopen2.write(line)
    infopen.close()
    outopen1.close()
    outopen2.close()


fenhang()
