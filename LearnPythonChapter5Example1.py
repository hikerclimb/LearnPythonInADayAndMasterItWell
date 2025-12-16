import sys
def main():
    average = 75
    if average >=70:
        print('enter A')
        grade = "A."
    elif average >=60:
        print('enter B')
        grade = "B."
    elif average >=50:
        print('enter C')
        grade = "C."
    elif average >=40:
        print('enter D')
        grade = "D."
    else:
        print('enter F')
        grade = "F."
    print(grade)
main()
