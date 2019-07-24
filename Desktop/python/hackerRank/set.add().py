n=int(input())
list2=set() #empty set , for list its '[]' and dict its '{}'
for i in range(0,n):
	b=str(input())
	list2.add(b) #add() function adds new element to set and is exclusively  set's function

print(len(list2))