import collections
n=int(input())
list2=collections.deque() # from collections import 
for i in range(0,n):
	list1=input().split()
	if list1[0]=='append':
		list2.append(list1[1])
	elif list1[0]=='pop':
		list2.pop()
	elif list1[0]=='appendleft':
		list2.appendleft(list1[1])
	elif list1[0]=='popleft':
		list2.popleft()
print(" ".join(list2))