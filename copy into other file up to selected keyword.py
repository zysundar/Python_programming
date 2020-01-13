def Copyfile(File1,File2):
    file1 = open("File1","r")
    file2 = open("File2","w")
    while True:
        text=file1.read(100)  #upto 100 char
        if text=="":  #Put your selected word
            break
        file2.write(text)
    file1.close()
    file2.close()
print(Copyfile("File1.txt","File2.txt"))
