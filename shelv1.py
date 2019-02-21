import shelve
fruit= shelve.open('sss') 
fruit['apple']="good for making cider"
fruit['lemon']="a sour,yellow citrous fruits"
fruit['lime']="a sour, green citrus frit"

#print(fruit['orange'])
'''while True:
    shelve_key=input("enter any fruits")
    if shelve_key=="quit":
        break
    if shelve_key in fruit:
        des=fruit.get(shelve_key,"we have not a fruit"+shelve_key)
        print(des)'''
'''for f in sorted(list(fruit.keys())):
    print(f+'  -'+fruit[f])'''
'''for v in fruit.values():
    print(v)
print(fruit.values())'''
fruit['ss']="sssss"
print(fruit['ss'])
print(fruit)

