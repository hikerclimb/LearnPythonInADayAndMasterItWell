def main():
    numberMatch = int(input("number to match:"))
    list_match = [1,2,3,4,5]
    print([x for x in list_match if numberMatch == x ])
main()
