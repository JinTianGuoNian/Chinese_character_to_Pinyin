# def remove_symbols(a, b):
#     file1 = open(a, 'r', encoding='utf-8')
#     file2 = open(b, 'w', encoding='utf-8')
#     try:
#         for line in file1.readlines():
#             print(len(line))
#     finally:
#         file1.close()
#         file2.close()
#
#
# remove_symbols('', '')
# =========================================================
# file_name = "D:/test/a_porject.py"
# file_name = file_name.split('.')[0]
# print(file_name)
#  ========================================================
# import os
#
# file_path = "../数据集/人民日报数据集/renmin2.txt"
# (filepath, tempfilename) = os.path.split(file_path)
# (filename, extension) = os.path.splitext(tempfilename)
#
# print((filepath, tempfilename))
#
# print((filename, extension))

#  ======================================================
# import os
#
# li = []  # 数据集列表
#
#
# def load_data(filepath):
#     # 遍历filepath下所有文件，包括子目录，路径的最后要加斜杆
#     files = os.listdir(filepath)
#     for fi in files:
#         fi_d = os.path.join(filepath, fi+'/')
#         if os.path.isdir(fi_d):
#             load_data(fi_d)
#         else:
#             li.append(fi_d[:-1])
#     return li
#
#
# load_data('D:/语料识别/语料库/维基百科语料库/wiki_zh/')
# print(len(li))
#
# for i in list(range(0, len(li))):
#
#     print(li[i])
#     file_path = li[i]
#     (filepath, tempfilename) = os.path.split(file_path)
#     (filename, extension) = os.path.splitext(tempfilename)
#
#     b = filepath + '/' + filename + '_汉字.txt'
#     c = filepath + '/' + filename + '_拼音.txt'
#
#     print(b)
#     print(c)
#

#  ==============================================================
# import re
#
# str1 = ''.join(re.split('\W+', "我在吃饭，你在干嘛？很高兴认识你！五一、十一放假10,000天：是吗？"))
# print(str1)

# ================================================================
# import json
#
# # with open('../数据集/wiki_00', 'r', encoding='utf-8') as file:
# #     # d读取文件，并转换成json格式
# #     html = file.read()
# #     html_json = json.loads(html)   # 以json形式加载
# #     print(type(html), type(html_json))
# #
# #     html_result = html_json["text"]
# #     print(html_result)
#
#
# data = []
# with open('../数据集/wiki_00', 'r', encoding='utf-8') as f:
#     for line in f:
#         data.append(json.loads(line))
#
# print(data[0]['text'])

# ================================================================
# 去除()[]{}以及里面内容
# import re
# s = "我是 (aaa) bbb [ccc] ddd {eee}"
# a = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", s)
# print(a)
# ================================================================

#  同一文件修改，汉字输出在拼音后面
# from pypinyin import lazy_pinyin, Style
# line_list = []
# file = open('test.txt', 'r', encoding='utf-8')
# for line in file.readlines():
#     line_new = " ".join(lazy_pinyin(line, style=Style.TONE)).replace('\n', '').strip()
#     line_new = line_new + '\t' + line  # 拼音加汉字
#     print(line_new)
#     line_list.append(line_new)
# print(line_list)
# file.close()
# file = open('test.txt', 'w', encoding='utf-8')
# try:
#     for i in list(range(0, len(line_list))):
#         file.write(line_list[i])  # 写入一个新文件中
# finally:
#     file.close()
# ==========================================================================
# from pypinyin import lazy_pinyin, Style
#
# a = '我有11个“【苹果】”'
# print(" ".join(lazy_pinyin(a, style=Style.TONE)).replace('\n', '').strip())
#
# =============================================================================
# import re
# from string import ascii_letters
#
#
# def remove_symbols(a, b):
#     file1 = open(a, 'r', encoding='utf-8')
#     file2 = open(b, 'w', encoding='utf-8')
#     try:
#         for line in file1.readlines():
#             my_re = re.compile(r'[0-9A-Za-z]', re.S)
#             res = re.findall(my_re, line)
#             if len(line) >= 3 and not len(res): # 控制每一行有两个或以上的汉字
#                 file2.write(line)
#     finally:
#         file1.close()
#         file2.close()
#
#
# remove_symbols('test.txt', 'test_2.txt')

#  ================================================================
# -*- coding:utf-8 -*-
# import re
#
#
# def check(str):
#     my_re = re.compile(r'[0-9A-Za-z]', re.S)
#     res = re.findall(my_re, str)
#     print(res)
#     if not len(res):
#         print('不含有英文和数字')
#
#
# if __name__ == '__main__':
#     str = '你好'
#     check(str)

#  =================================================================
import json


file1 = open('D:/语料识别/语料库/test/wiki_00', 'r', encoding='utf-8')
file2 = open('D:/语料识别/语料库/test/wiki_00.txt', 'w', encoding='utf-8')
for line in file1:
    a_line = json.loads(line)
    b_line = a_line['title'] + '\n'
    file2.write(b_line)

file1.close()
file2.close()
