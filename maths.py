from fractions import gcd
from math import *

def lcm(a, b):
	return a*b / gcd(a,b)
	
def gcd(a,b):
	"""Returns the greatest common divisor of a and b"""
	return fractions.gcd(a,b)

def sieveofera(limit):
        """
            Implements a naive sieve of Eratosthenes finding primes
            less than n
        """
        a = [True]*limit
        ret = []

        for i in xrange(2,len(a)):
            if a[i]:
                yield i
                for j in xrange(i*i, limit, i):
                    a[j] = False
                
