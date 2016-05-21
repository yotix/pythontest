def reversehash(h):
    s = []
    a = 'acdegilmnoprstuw'
    for x in xrange(9):
        s.append(a[h%37])
        #print a[h%37]
        h = (h-h%37)/37
    s.reverse()
    return ('').join(s)
    
print reversehash(930846109532517)
