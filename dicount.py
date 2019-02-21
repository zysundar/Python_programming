s="sdsfescwerfsegwew2rwfweg"
lc={}
for let in s:
    lc[let]=lc.get(let,0)+1
#print(lc)
l=lc.items()
l.sort()
print(l)
