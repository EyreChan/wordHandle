import json
from pypinyin import lazy_pinyin

from wordHomophone import w_homophone

pcorpus = open("phraseyes.txt", "r", encoding='gbk')

datalist1 = []
datalist2 = []

for line in pcorpus:
    plist = line.rstrip().split(" ")
    py_list = lazy_pinyin(plist)

    # list转字符串
    plist = "".join(plist)
    py_list = " ".join(py_list)

    datalist1.append(plist)
    datalist2.append(py_list)

p_homophone = {}
for i in range(0, len(datalist1), 1):
    if datalist2[i] not in p_homophone:
        p_homophone[datalist2[i]] = []
        p_homophone[datalist2[i]].append(datalist1[i])
    else:
        if datalist1[i] not in p_homophone[datalist2[i]]:
            p_homophone[datalist2[i]].append(datalist1[i])
        else:
            pass

#合并字词混淆集
t_homophone = dict(w_homophone, **p_homophone)

#保存为json文件
with open("homophone.json","w",encoding='utf-8') as f:
    f.writelines(json.dumps(t_homophone, ensure_ascii=False, indent=4))

pcorpus.close()
