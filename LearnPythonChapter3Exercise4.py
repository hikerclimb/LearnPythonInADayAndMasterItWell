def main():
    dictionary1 = {1:20, 4:40}
    dictionary2 = {6:60, 8:80}
    dictionary3 = {10:100, 12:120}
    dictionaryfinal = dictionary1 | dictionary2 | dictionary3
    print(dictionaryfinal)
main()
