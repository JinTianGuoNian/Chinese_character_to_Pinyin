import json
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


load_data('D:/语料识别/语料库/维基百科语料库/wiki_zh/')
print(len(li))

for i in list(range(0, len(li))):
    print(li[i])
    file_path = li[i]
    (filepath, tempfilename) = os.path.split(file_path)
    (filename, extension) = os.path.splitext(tempfilename)

    b = filepath + '/' + filename + '.txt'
    # b = '../数据集/wiki_zh/AC/' + filename + '.txt'

    data = []
    with open(li[i], 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))

    file = open(b, 'w', encoding='utf-8')
    try:
        for j in list(range(0, len(data))):
            file.writelines(data[j]['text'])
    finally:
        file.close()
