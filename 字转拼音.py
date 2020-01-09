# coding:utf-8
from pypinyin import pinyin, lazy_pinyin, Style

a = '哈工大信息检索研究室汉英双语语料库_样例_偶数行_去标点_去空行.txt'

b = a[:-4] + '_转拼音' + a[-4:]


def word_to_pinyin():
    file1 = open(a, 'r', encoding='utf-8')
    file2 = open(b, 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            line = " ".join(lazy_pinyin(line, style=Style.TONE))
            file2.write(line)
    finally:
        file1.close()
        file2.close()


word_to_pinyin()
