#Creates base operations questions
import random as r
operations = ['*', '-', '+', '/']
options = [2, 8, 10, 16]
b = ""
lim = r.randint(2, 10)
leng = r.randint (2, 10)
for i in range (leng):
	a = r.randint(0, lim-1)
	c = str(a)
	b += c
print b, "base", lim, 
print r.choice(operations), 
b = ""
lim = r.randint(2, 10)
leng = r.randint (2, 10)
for i in range (leng):
	a = r.randint(0, lim-1)
	c = str(a)
	b += c
print b, "base", lim, 
print r.choice(operations), 
b = ""
lim = r.randint(2, 10)
leng = r.randint (2, 10)
for i in range (leng):
	a = r.randint(0, lim-1)
	c = str(a)
	b += c
print b, "base", lim, 
print "answer in base ", r.choice(options)
