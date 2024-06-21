i = 9
while i > 6:
	a = i
	b = i - 3
	c = i - 6
	j = 1
	while j < 10:
		print('%d x %d = %d' % (a, j, a*j), end='\t')
		print('%d x %d = %d' % (b, j, b*j), end='\t')
		print('%d x %d = %d' % (c, j, c*j))
		j += 1
	print()
	i -= 1 


