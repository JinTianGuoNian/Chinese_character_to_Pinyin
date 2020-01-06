# coding:utf-8
from zhon.hanzi import punctuation as zp
from string import punctuation as sp
from string import digits

a = '哈工大信息检索研究室汉英双语语料库_样例_偶数行.txt'

b = a[:-4] + '_去标点' + a[-4:]


def remove_symbols():
    file1 = open(a, 'r', encoding='utf-8')
    file2 = open(b, 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            a_num = digits
            b_num = '零一二三四五六七八九'
            tran_sum = str.maketrans(a_num, b_num)

            del_estr = zp + sp  # 中文标点符号，英文标点符号
            replace = "\n" * len(del_estr)
            tran_tab = str.maketrans(del_estr, replace)

            line = line.translate(tran_sum)
            line = line.translate(tran_tab)
            file2.writelines(line)
    finally:
        file1.close()
        file2.close()


remove_symbols()


# def remove_symbols(sentence):
#     del_estr = zp + string.punctuation + string.digits + ' '  # 中文标点符号，英文标点符号，空格
#     replace = "\n" * len(del_estr)
#     tran_tab = str.maketrans(del_estr, replace)
#     sentence = sentence.translate(tran_tab)
#     return sentence
#
#
# print(remove_symbols('"刚才 我看见你123把一根吸了一半的香烟扔过了墙，是吗，彼得？""我怎么了，先生？"他答道，一副受冤枉的样子。'))
