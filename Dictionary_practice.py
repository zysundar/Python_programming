imoprt operator

dic={"name":"Mike","age":20,"address":"lpu"}
print dic

di={"name":"Dustin","age":20,"address":"lpu",(1,5):"tuple"}
print di

ic={ " ":"Will","age":20,"address":"lpU"}
print ic

dic1={}
for i in (dic,di,ic):
    dic1.update(i)
print(dic1)

print di["name"]

d={1:2,4:9,5:3,7:8,2:6}
print d.keys()
print("original dictionary",d)

sorted_d=sorted(d.items(),key=operator.itemgetter(0))
print ("ascending order",sorted_d)


dic2={}
for var in key(1,16):
    dic2.update(var*var)
print dic2


