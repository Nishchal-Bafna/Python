n=int(input('enter range of an array'))                                                   # input for length of an array
a=[0 for i in range(n)]                                                                   # initiallizing the array of length n(all values assigned as 0)

for i in range(n):                                                                        # for loop to take values of an array
	a[i]=int(input('{} elment   '.format(i+1)))                                       # inserting elements in an array
sum=int(input('enter a sum'))                                                             # taking sum from user to search for

def check(a,n,sum):                                                                       # defination of function
	for i in range (n):                                                               # for loop to calling elements of array
		cur_sum=a[i]                                                              # storing the 1st value of array in temprary variable
		j=i+1                                                                     # for taking next values to add so increasing j
		while j<n:                                                                # while conditioon to excute loop continuously
			if cur_sum==sum:                                                  # checking condition for expected sum is getting or not
				print('sum found between index {} to {}'.format(i,j-1))   # print statement to print the index where sum was found
				return 1                                                  # returning back from fuction
			if cur_sum>sum:                                                   # checking condition sum is exceeding or not
				break                                                     # if sum is exceeding then terminating while loop for that index
			cur_sum=cur_sum+a[j]                                              # storing the calculated sum in temprory vcariable
			j=j+1                                                             # increasing the value of j for next sum
	print('not found')                                                                # if sum was not found then print this statement

check(a,n,sum)                                                                            # calling the function





'''
output
enter range of an array = 9
enter 1 element  1
enter 2 element  5
enter 3 element  3
enter 4 element  4
enter 5 element  9
enter 6 element  2
enter 7 element  7
enter 8 element  6
enter 9 element  5
( 1+1=2 ) ; ( 1+5=6 ) ; ( 1+3=4 ) ; ( 1+4=5 ) ; ( 1+4=5 ) ; ( 1+2=3 ) ; ( 1+6=7 ) ; ( 1+5=6 ) ; ( 5+4=9 ) ; ( 5+2=7 ) ; ( 3+3=6 ) ; ( 3+4=7 ) ; ( 3+2=5 ) ; ( 3+2=5 ) ; ( 3+6=9 ) ; ( 4+2=6 ) ; ( 4+5=9 ) ; ( 2+2=4 ) ; ( 2+7=9 ) ; ( 2+5=7 ) ; so the count is =  20
'''
