class Number:
    def __init__(self, target):
        self.target = target

    def matchTotalFrom2Numbers(self):
        givenArray = [1,2,5,7,5]
        found = False
        for i in givenArray:
            for index,value in enumerate(givenArray, start=1):
                if i + value == self.target:
                    print(self.target)
                    found = True
                    break
            if found:
                break  

class myclass:
    def twoSum_function(self, num, target):
        lookup = {}
        for index, num in enumerate(num):
            if target - num in lookup:
                return (lookup[target-num]+1, index+1)
            lookup[num] = index

def main():
    matchNumber= Number(12)
    str(matchNumber.matchTotalFrom2Numbers())
    print(myclass().twoSum_function((20,20,10,70,100,60,70),40))

main()

