#Given a number and a base convert it into base 2, 8, 10, 16
import random as r
print "Convert the following numbers into bases 2, 8, 10, and 16: "
for j in range (20): 
	lim = r.randint(2, 10)
	leng = r.randint (2, 10)
	b = ""
	for i in range (leng):
		a = r.randint(0, lim-1)
		c = str(a)
		b += c
	print b, "( base", lim , ")"

