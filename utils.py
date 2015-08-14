	
def change_speed(frequency, wave):
	return lambda x : wave(x*frequency)
	
def mul(f, g):
	return lambda x : f(x) * f(g)
	
def add(f, g):
	return lambda x : f(x) + f(g)
	
	