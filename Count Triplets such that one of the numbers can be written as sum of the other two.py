n=int(input('enter range of an array = '))
a=[0 for i in range (n) ]


def check():
	m=0
	for i in range(n):
		for j in range(i,n):
			z=a[i]+a[j]
			for k in range(n):
				if z==a[k]:
					m = m+1
					print('( {}+{}={} ) ;'.format(a[i],a[j],a[k]),end=' ')
	print('so the count is = ',m)
	

for i in range(0,n):
	a[i]=int(input('enter {} element  '.format(i+1)))
check()



'''
output
enter range of an array = 6
enter 1 element  1
enter 2 element  2
enter 3 element  3
enter 4 element  4
enter 5 element  5
enter 6 element  6
( 1+1=2 ) ; ( 1+2=3 ) ; ( 1+3=4 ) ; ( 1+4=5 ) ; ( 1+5=6 ) ; ( 2+2=4 ) ; ( 2+3=5 ) ; ( 2+4=6 ) ; ( 3+3=6 ) ; so the count is =  9
'''
