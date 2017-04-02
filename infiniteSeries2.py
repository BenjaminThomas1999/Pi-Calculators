series = 0
k = 1
add = True
pi=0

while True:
	if add:
		series += 1/k
	else:
		series -= 1/k
	k+=2
	add = not add
	
	pi = 4*series
	print(pi)