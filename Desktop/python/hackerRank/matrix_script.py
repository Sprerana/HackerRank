import re
a=input().split()
x=int(a[0])
y=int(a[1])
j=0
p=0
t=[]
list1=[]
list2=[]
f=[]
for i in range(x):
	x=list(input())
	t.append(x)
print(t)
while(j<y):
	for k in range(0,len(t)):
		p=t[k][j]
		list1.append(p)
	j=j+1
print(list1)	
p=str(''.join(list1))

k=re.search("[a-zA-Z][!|@|#|$|%|&|\s]+[a-zA-Z]",p)
print(k.end())
for i in range(k.end()):
	x=p[i].replace("#"," ")
	list2.append(x)
	print(x,end=' ')
for a in range(len(p)-k.end()):
	z=list1[a+k.end()]
	f.append(z)
print(f)
s=list2+f
print(''.join(s))


#IMPORTANT CONCEPTS: 1.re package 2.methods like search,match,findall 3.replace method in string 4.visualization of the problem 
#FIRST THINK,MAKE UP YOUR MIND AND THEN CODE!!!
	