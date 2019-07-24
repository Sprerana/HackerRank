n=int(input())
list1=[]
list2=set()

for i in range(0,n):
	b=str(input())
	list1.append(b)
	list2.add(b)
	
list3=set(list1)
list4=list(list3)
print(len(list2))
for j in range(0,len(list4)):
	print(list1.count(list4[j]),end=' ')


	
	