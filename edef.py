def main():
    a=input()
    if isinstance(a,int):
        print("This input is of type Integer")
    elif isinstance(a,str):
        print("This input is of type String")
    elif isinstance(a,float):
        print("This input is of type Float")
    else:
        print("This input is something else")
main()
