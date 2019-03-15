while True:
    test = input().split()
    if test == ['0','0']:
        break
    print(str(int(test[0]) + int(test[1])))