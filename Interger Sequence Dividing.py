n = int(input())

sum = 0

if n>4:

	if ((n-1)%4==0 or (n-2)%4==0):
		print(1)

	else:
		print(0)

elif n<=4 and n>1:
	for i in range(1, n+1):
		sum = sum + i

	if sum%2==0 :
		print(0)

	else :
		print(1)	
		
elif n==1:
    print(1)