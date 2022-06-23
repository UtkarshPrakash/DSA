t = int(input())
for q in range(t):
	n = int(input())
	count=0
	if (n%2==0):
		count = (n/2)-1
		#for i in range(int(n/2)+1,n):
		#	count += 1
	else :
		count = int(n/2)
		#for j in range(int(n/2)+1,n):
		#	count += 1
	print(int(count))				