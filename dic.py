import string
dic={}
dic.update({1:2})
dic[2]=3
dic[4]=8
dic[5]=9
print(dic)
del dic[2]
print(dic)
print(sum(dic.value()))
    
item=dic.items()
d=item.sort()
print(d)
sorted_d=sorted(dic.items(),key=operator.itemgetter(0))
print (sorted_d)
