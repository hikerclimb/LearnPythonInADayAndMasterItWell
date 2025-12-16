

def factorialRecursive(num):
    if num == 1:
        return 1
    else:
        return num * factorialRecursive(num -1)
    
def factorialLoop(num):
    multiply = 1
    if num ==1:
        return 1
    else:
        for i in range(1, num+1):
            multiply *= i 
    return multiply
