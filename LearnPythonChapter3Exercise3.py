def main():
    lst = ['John', 'Peter', 'Sam', 'Tim', 'Janet', 'Dan']
    lst = [x for (i,x) in enumerate (lst) if i not in (0,4,5)]
    print(lst)
main()
