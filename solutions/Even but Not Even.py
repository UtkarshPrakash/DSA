def even_digits(lis) : #function to return sum of elements of list
	add = 0
	for kk in lis :
		if (int(kk)%2 == 0) :
			add = add + 1

	return add	

t = int(input()) #input no. of test cases
#count = -1

for k in range(t) :
	n = int(input()) #No of digits in original number
	ss = (input()) #Original Number
	s_list = list(ss) #Converted to string value so that extend() can be used
	s = []
	s.extend(s_list) #Original number converted to list
	(sum_s) = 0
	for l in s :
		sum_s = sum_s + int(l)

	if ((int(sum_s)%2 == 0) and (int(ss)%2 != 0)): #If ebne, print as it is
		print(ss)

	elif (n == 1) : #If single digit no. print(-1)
		print(-1)

	elif (even_digits(s) == n) :	# If every digit is even, print(-1)
		print(-1)

	else :
		count = -1
		if ((int(s[-1])%2 != 0)) : #If original number is odd
			for ll in s :
				#count = count + 1
				if (int(ll)%2 != 0) :
					s.remove(ll)
					continue

			for rt in s :
				print(rt, end = '')		


		elif (int(s[-1]%2) == 0) : #If original number is even
			while (int(s[-1]%2) == 0) :
				del s[-1]

		for rt in s :
			print(rt, end = '')		
	
			
	print('\n')		