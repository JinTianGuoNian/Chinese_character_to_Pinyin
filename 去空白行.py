# coding = utf-8

a = '哈工大信息检索研究室汉英双语语料库_样例_偶数行_去标点.txt'

b = a[:-4] + '_去空行' + a[-4:]


def clearBlankLine():
    file1 = open(a, 'r', encoding='utf-8')
    file2 = open(b, 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


clearBlankLine()
