corpus = open('phraseno.txt', 'r', encoding = 'gb18030')
txtbuffer = corpus.read()

oldlist = ['']
newlist = ['']
oldlist = list(txtbuffer)
for i in range(0, len(txtbuffer), 1):
	if oldlist[i] == "[":
		for j in range(1, 30, 1):
			if oldlist[i + j] == "]":
				newlist.append("\n")
				break
			newlist.append(oldlist[i + j])
#print(newlist)
phralist="".join(newlist)
txtnew=open("phraseyes.txt","w")
txtnew.write(phralist)
txtnew.close()
corpus.close()
