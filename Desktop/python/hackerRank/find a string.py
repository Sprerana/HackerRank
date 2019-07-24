str1=str(input())
str2=str(input())
count=0

for i in range(0,len(str1)):
	for j in range(i+1,len(str1)):
		if str2==str1[i:j+1]:
			count=count+1
print(count)
		