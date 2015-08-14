import math

def square(x):
	if x%1.0 < 0.5:
		return 1.0
	else:
		return 0.0
	
def triangle(x):
	x = x%1.0
	if x < 0.5:
		return 4.0*x - 1.0
	else:
		return 1.0 - 4.0*(x-0.5)
	
def saw(x):
	return (x%1.0)*2.0 - 1.0

def sin(x):
	return math.sin(x/(math.pi*2.0))