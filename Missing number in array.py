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
			if a[i]!=z[i]:
				print('missing no is ',z[i])
				return(1)
	missing_no_check()
	w=w-1
  
  '''
  output
  how many test case you want to perform2
enter range of an array5
0 element 1
1 element 2
2 element 3
3 element 5
[1, 2, 3, 5, 0]
[1, 2, 3, 4, 5]
missing no is  4
enter range of an array10
0 element 1
1 element 2
2 element 3
3 element 4
4 element 5
5 element 6
6 element 8
7 element 9
8 element 10
[1, 2, 3, 4, 5, 6, 8, 9, 10, 0]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
missing no is  7

  
  '''
