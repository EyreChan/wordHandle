datalist1 = []
datalist2 = []
wcorpus = open("wordyes.txt", "r", encoding='utf-8-sig')

for line in wcorpus:
    wlist = line.strip().split(" ")
    datalist1.append(wlist[0])  #每行首元素为读音
    datalist2.append(wlist[1:]) #其余元素为同音字

#生成汉字同音混淆集
w_homophone = dict(zip(datalist1, datalist2))

wcorpus.close()