#!/usr/bin/env python
"""Module for number theory procedures"""

from fractions import gcd
from math import *
from random import randint

__author__ = "rmanders"
__status__ = "Development"

# =============================================================================
#             L C M
# =============================================================================
def lcm(a, b):
	"""Returns least common multiple based on gcd function"""
	return a*b / gcd(a,b)
	
# =============================================================================	
#             G C D
# =============================================================================
def gcd(a,b):
	"""Returns the greatest common divisor of a and b"""
	return fractions.gcd(a,b)
	
# =============================================================================
#             E X T E N D E D    G C D
# =============================================================================
def egcd(a, b):
	"""
	Extended GCD: returns a 2-tuple (x,y) for inputs a, b such that:
	ax + by = gcd(a,b)
	"""
	x = 0
	y = 1
	lx = 1
	ly = 0
	while b != 0:
		q = a // b
		a,b = b,a%b
		x,lx = lx-(q*x),x
		y,ly = ly-(q*y),y
	return (lx,ly)

# =============================================================================
#             S I E V E   OF   E R A T O S T H E N E S
# =============================================================================
def sieveofera(limit):
        """
            Implements a naive sieve of Eratosthenes generator finding primes
            less than limit
        """
        a = [True]*limit
        ret = []

        for i in xrange(2,len(a)):
            if a[i]:
                yield i
                for j in xrange(i*i, limit, i):
                    a[j] = False

# =============================================================================
#             F I R S T   N   P R I M E S
# =============================================================================
def firstnprimes(n, limit=500):
	"""
	Gets a list of the first n primes in sorted order that are less than limit
	"""
	ret = []
	for p in sieveofera(limit):
		ret.append(p)
		if len(ret) >= n:
			return ret
	raise Exception("Prime limit exceeded")

# =============================================================================
#             P R O D U C T   O F   P R I M E S
# =============================================================================
def primeprod(maxp, limit=1000):
	"""
		Generates a list of the smallest primes such that their 
		product is greater than maxp.
	"""
	p = []
	prod = 1
	for i in sieveofera(limit):
		prod *= i
		p.append(i)
		if prod > maxp:
			return p
	raise Exception('Prime limit exeeded')

# =============================================================================
#             D I S C R E T E   E X P O N E N T I A L 
# =============================================================================
def dexp(a, x, n):
	"""Discrete exponential. Finds a^x mod n"""
	e = 1
	while x != 0:
		if x % 2 == 1:
			e = (e*a) % n
			x = x-1
		a = (a**2) % n
		x = x // 2
	return e

# =============================================================================	
#             C H I N E S E   R E M A I N D E R   T H E O R E M
# =============================================================================
def gencrt(a=[], m=[]):
	"""
	Solves a generalized system of congruences using the chinese remainder 
	theorem such that x (congruent to) a[i] mod m[i] where a[] is a list of 
	congruences and m[] is a list of pairwise coprime moduli.
	"""
	#TODO: Add a check for pairwise coprime moduli and throw an 
	#      exception if failed.
	
	M=reduce(lambda x,y: x*y, m)
	x = 0
	for i in xrange(len(m)):
		j,k = egcd(m[i], (M//m[i]))
		e = (1-(j*m[i]))
		print "e =", e
		x += a[i]*e
	return x % M
