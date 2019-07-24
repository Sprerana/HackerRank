n=int(input())
def binary(n):
	if n>1:
		binary(n//2)
	print(n%2,end='')

for i in range(1,n+1):
	print(str(i)+" "+str(oct(i))+" "+str(hex(i))+" "+str(bin(i))+" ")
	