def main():
    input1 = int(input("enter first number:"))
    input2 = int(input("enter second number:"))
    input3 = int(input("enter third number:"))
    sum = 0
    if (input1 == input2 or input2 == input3 or input1 == input3):
        sum = 0
    else:
        sum = input1 + input2 + input3
    print(sum)
main()
