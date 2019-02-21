f=open("sss.txt","r+")
print "Name of th efile ",f.name()



for index in range(5):
    line=f.next()
    print "line no %d - %s"%(index,line)
    f.close()
