def main():
    for numb in range(2, 13):
        print(primeOrNot(numb))

def primeOrNot(num):
    if  num > 1:
        counter = True
        for i in range(2,num):
            if  num%i == 0:
                counter = False
                break
        print('"' + str(num) + ':"' + str(counter))
main()
