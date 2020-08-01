n=int(input('enter the range of an array'))
a=[0 for i in range (n+1)]
b=[]

for i in range(n):
	a[i]=int(input('enter {} element = '.format(i+1)))

def kadane():
	sum=0
	z=0
	s=0
	start=0
	end=0
	for i in range(n):
		sum=sum+a[i]
		if sum>z:
			z=sum
			start=s
			end=i
		
		if sum<0:
			sum=0
			s=i+1

	print('largest sum in contiguous array = ',z)
	print('array is in between index {} , {}'.format(start,end))
	print('elements of arrays are')
	for i in range(start,end+1):
		b.append(a[i])
	print(b)	
kadane()
		
    
    
'''
output
enter the range of an array8
enter 1 element = -2
enter 2 element = -5
enter 3 element = 6
enter 4 element = -3
enter 5 element = -4
enter 6 element = 5
enter 7 element = 6
enter 8 element = -2
largest sum in contiguous array =  11
array is in between index 5 , 6
elements of arrays are
[5, 6]
'''
		
