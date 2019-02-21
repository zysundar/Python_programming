def main():
    d = input("Enter Numbers: ").split()
    d = list(set(d))
    d = map(int, d)
    print(d)
main()
