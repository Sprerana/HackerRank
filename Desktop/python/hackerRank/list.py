a=int(input())
list1=[]
for i in range(0,a):
	list2=input().split()
	b=str(list2[0])
	
	c="print"
	d="insert"
	e="reverse"
	f="append"
	g="pop"
	if b==d:
		list1.insert(int(list2[1]),int(list2[2]))
	elif b==e:
		list1.reverse()
	elif b==f:
		list1.append(int(list2[1]))
	elif b==g:
		list1.pop()
	elif b==c:
		print(list1)
	
		