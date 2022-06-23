n = (input())

def sum_digits(l):
	m = list(str(l))
	sum = 0
	arr=[]
	arr.extend(m)
	for i in arr:
		sum = sum + int(i)

	return sum
		

if (sum_digits(n)%4==0) :
	print(n)

elif (sum_digits(int(n)+1)%4==0) :
	print(int(n)+1)

elif (sum_digits(int(n)+2)%4==0):
	print(int(n)+2)

elif (sum_digits(int(n)+3)%4==0):
	print(int(n)+3)				
	
elif (sum_digits(int(n)+4)%4==0):
	print(int(n)+4)	
	
elif (sum_digits(int(n)+5)%4==0):
	print(int(n)+5)	
	
elif (sum_digits(int(n)+6)%4==0):
	print(int(n)+6)		
	
elif (sum_digits(int(n)+7)%4==0):
	print(int(n)+7)			