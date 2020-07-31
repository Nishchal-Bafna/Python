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
