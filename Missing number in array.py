w=int(input('how many test case you want to perform'))
while w!=0:
	a=[]
	n=int(input('enter range of an array'))
	for i in range(n-1):
		z=int(input('{} element '.format(i)))
		a.append(z)
	a.append(0)
	print(a)
	def missing_no_check():
		z=list(range(1,n+1))
		print(z)
		for i in range(n):
			b=z[i]
			for j in range(n):
				if a[j]==b:
					break
				else:
					if j==n-1:
						print('missing no is ',b)
					
	missing_no_check()
	w=w-1
  
  '''
  output
how many test case you want to perform1
enter range of an array7
0 element 1
1 element 7
2 element 5
3 element 4
4 element 2
5 element 3
[1, 7, 5, 4, 2, 3, 0]
[1, 2, 3, 4, 5, 6, 7]
missing no is  6

  
  '''
