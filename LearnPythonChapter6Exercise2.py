def main():
    for numb in range(2, 20):
        print(primeOrNot(numb))

def primeOrNot(num):
    if  num > 1:
        counter = False
        for i in range(1,num + 1):
            print('enter')
            if  num%i == 0:
                #print('numtrue:' + str(num)+ 'i:' + str(i))
                counter = True
            elif num % i == 1:
                #print('numfalse1:' + str(num)+ 'i:' + str(i))
                counter = False
                break
        print('counter:' + str(counter))
main()
