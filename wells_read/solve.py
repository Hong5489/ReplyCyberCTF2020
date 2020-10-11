ori = open("original.txt",'r').read().split()
text = open("The Time Machine by H. G. Wells.txt",'r').read().split()
words = open("words.txt").read().split("\n")
flag = ""
for o,t in zip(ori,text):
	if o!=t:
		for c1,c2 in zip(o,t):
			if c1 != c2:	
				flag += c2
				break
print(flag)