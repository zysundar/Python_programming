def maxx(x,y):
    if(x>y):
        return x
    else:
        return y
def maxx_three(x,y,z):
    return maxx(x,maxx(y,z))
print(maxx_three(5,8,5))
