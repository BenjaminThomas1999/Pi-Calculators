import math
series = 0
k = 1
while True:
	series += 1/(k**2)
	pi = math.sqrt(series*6)
	print(pi)
	k += 1