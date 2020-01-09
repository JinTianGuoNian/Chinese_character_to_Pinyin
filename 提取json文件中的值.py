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


load_data('D:/语料识别/语料库/baike_qa2019/')
print(len(li))

for i in range(0, len(li)):
    # file_path = li[i]
    # (filepath, tempfilename) = os.path.split(file_path)
    # (filename, extension) = os.path.splitext(tempfilename)

    b = 'D:/语料识别/语料库/baike_qa2019_answer/' + str(i) + '.txt'
    # b = filepath + '/' + filename + '.txt'

    file1 = open(li[i], 'r', encoding='utf-8')
    file2 = open(b, 'w', encoding='utf-8')
    for line in file1:
        a_line = json.loads(line)
        b_line = a_line['answer'] + '\n'
        file2.write(b_line)

    print(b)
    file1.close()
    file2.close()

