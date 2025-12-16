def main():
    numbers = [1,2,3,4]
    countEven = 0
    countOdd = 0
    for num in numbers:
        if num % 2 == 0:
            countEven = countEven+num
        else:
            countOdd = countOdd+num

    print('countEven:' + str(countEven))
    print('countOdd:' + str(countOdd))
main()
