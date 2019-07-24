n=input()
c=0
if len(n)==6:
	for i in range(0,len(n)-2):
		if n[i]==n[i+2]:
			c+=1
	if c==1:
		print("valid")
	else:
		print("invalid")