str1=str(input())
n=len(str1)
k=int(input())
j=int(n/k)
i=0
while(i<n):	
	print("".join(set(str1[i:i+j]))) #join fucntion can change the format of strings the way we want
	i=i+j
str1=str(input())
n=len(str1)
k=int(input())
j=int(n/k)
i=0
while(i<n):	
	print("".join(set(str1[i:i+j]))) #join fucntion can change the format of strings the way we want
	i=i+j
