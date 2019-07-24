str1=str(input())
list1=list(str1)
b=[]
c=[]
d=[]
e=[]
for i in range(0,len(list1)):
	if list1[i].isupper(): 
		b.append(list1[i])
	if list1[i].islower():
		c.append(list1[i])
	if list1[i].isdigit():
		f=int(list1[i])
		if f%2==0:
			d.append(list1[i])
		else:
			e.append(list1[i])
c.sort()
b.sort()
e.sort()
d.sort()
print("".join(c+b+e+d))
	



