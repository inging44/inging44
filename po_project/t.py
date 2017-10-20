import string
def min(A):	
	 A.sort()
	 count = len(A)
	 max = A[count-1]
	 if max <0:
	 	return 1
	 B = range(1,max+2)
	 for i in B:
	 	if i in A:
	 		continue
	 	else:
	 		return i
# print sss([-1,0,2,5])

def x(num):
	r = []
	while num>=1:
		r.append(num%2)
		num = num/2
	r = r[::-1]
	num_1 = r.index(1)
	print num_1
	str1 = ''
	str1 = ''.join(map(str,r[::-1]))
	if '01' not in str1:
		return 0
	# print "str1",str1
	i = 0
	indexs = []


	while i <len(str1):
		index_1 = str1.find('1',i)
		if index_1 !=-1:
			indexs.append(index_1)
			i = index_1+1
	# print "indexs:",indexs
	
	a = [indexs[i+1]-indexs[i] for i,k in indexs]
	return a
print "a:",x(9)
