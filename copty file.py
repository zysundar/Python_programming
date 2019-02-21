def copyfile(su,ss):
    f1=open("su.txt","r")
    f2=open("ss.txt","w")
    while True:
        text=f1.read(34)
        if text=="":
            break
        f2.write(text)
    f1.close()
    f2.close()
print(copyfile("su.txt","ss.txt"))
