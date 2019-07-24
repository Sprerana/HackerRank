n=int(input())
a=set(input().split())
k=int(input())
for i in range(0,k):
	list1=input().split()
	if list1[0]=='pop':
		a.pop()
	elif list1[0]=='remove':
		a.remove(list1[1])
	elif list1[0]=='discard':
		a.discard(list1[1])
b=list(a)
for j in range(0,len(b)):
	sum1=0
	sum1=sum1+int(b[j])
print(sum1)

#!!!!pop in LIST removes LAST ELEMENT , but in SET removes RANDOM 	