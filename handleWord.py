import re
py_list = open('wordno2.txt', 'r',encoding='utf-8')#读取文本路径
dict = open('wordyes.txt', 'w', encoding = 'utf-8')
for line in py_list:
    infol = re.findall(r'[\u4e00-\u9fa5]|[a-zA-Z]{1,6}',line)
    for str in infol:
        dict.write(str + ' ')
    dict.write('\n')
py_list.close()
dict.close()