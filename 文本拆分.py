# 将一个大文本文件进行拆分，每10000行一次拆分


file1 = open('D:/语料识别/语料库/new2016zh/news2016zh_train.json', 'r', encoding='utf-8')
lines = file1.readlines()
try:
    for j in range(0, (len(lines)//10000)+1):
        file2 = open('D:/语料识别/语料库/new2016zh/train_' + str(j) + '.json', 'w', encoding='utf-8')
        print(10000 * (j + 1), '/', len(lines))
        for line in lines[10000*j: 10000*(j+1)]:
            file2.write(line)
        file2.close()
finally:
    file1.close()
