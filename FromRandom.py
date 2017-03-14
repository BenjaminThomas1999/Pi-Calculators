# The probability of two numbers being coprime is 6/(pi^2) http://mathoverflow.net/questions/97041/what-is-the-probability-that-two-numbers-are-relatively-prime
# Rearranging this for pi gives you pi = sqrt(6/(Probability of being coprime))
# Below is a program that calculates this strange relationship using random numbers and seeing if they are coprime
# Essentially derriving pi from random numbers

from fractions import gcd
from math import sqrt
from random import randrange, seed

seed()

coprime, total = 1, 0 # counters
limit = 1000000 # The higher the limit the more accurate your result
selected = [0, 0]

while True:
	selected = [randrange(limit), randrange(limit)]
	if gcd(selected[0], selected[1]) == 1:
		coprime += 1
	total += 1
	pi = sqrt(6/(coprime/total))
	print(pi)