from fractions import gcd

def lcm(a, b):
	return a*b / gcd(a,b)
	
def gcd(a,b):
	"""Returns the greatest common divisor of a and b"""
	return fractions.gcd(a,b)
