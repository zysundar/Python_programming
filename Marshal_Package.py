#Marshal module contains functions that can read and write Python values in a binary format.

import marshal
# Python code to demonstrate serialization
file1 = open("file1.txt","w")
bytes = marshal.dump([1,2,3,4,5],file1)
print bytes
file1.close()

# Python code to demonstrate de-serialization 
file2 = open("file1.txt","r")
bytes1 = marshal.load(file2)
print bytes1
file2.close()
