#!/usr/bin/python
import random

def hash(s):
    h = 9
    t = 'acdegilmnoprstuw'
    for x in xrange(len(s)):
        h = (h*37+t.index(s[x]))
    return h 
    pass

def reversehash(h):
    s = []
    a = 'acdegilmnoprstuw'
    for x in xrange(9):
        s.append(a[h%37])
        #print a[h%37]
        h = (h-h%37)/37
    s.reverse()
    return ('').join(s)

def unittesting():
    a = 'acdegilmnoprstuw'
    s = ''
    for x in xrange(9):
        s += a[random.randrange(0,16,2)]
    print reversehash(hash(s)) == s,hash(s),s,reversehash(hash(s))
    
for x in xrange(10):
    print unittesting()
