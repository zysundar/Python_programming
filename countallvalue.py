from collections import Counter
d=Counter([1,2,3,4,1,2,3,2,4,1,5,6,4,5,7,5])
d1=Counter(['cakewalk','simple','easy','easy-medium','medium','medium-hard','hard'])
l=set([1,2,3,4,1,2,3,2,4,1,5,6,4,5,7,5])
l1=Counter(['cakewalk','simple','easy','easy-medium','medium','medium-hard','hard'])
for i in l1:
    print(d1[i])
#print(d.most_common())
#print(d.most_common(1))
#print(max(d.values()))
