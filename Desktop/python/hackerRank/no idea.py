n=input().split()
a=set
count=0
a=input().split()
b=input().split()
c=input().split()
for i in range(0,len(a)):
	for j in range(0,len(b)):
		if a[i]==b[j]:
			count=count+1
	for k in range(0,len(c)):
		if a[i]==c[k]:
			count=count-1
print(count)