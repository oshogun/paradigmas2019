while True:
    num_tests = int(input())
    if num_tests == 0: 
        break
    divisa = input().split()
    divisa[0] = int(divisa[0])
    divisa[1] = int(divisa[1])
    for i in range(0, num_tests):
        point = input().split()
        point[0] = int(point[0])
        point[1] = int(point[1])

        if(point[0] == divisa[0] or point[1] == divisa[1]):
            print("divisa")
        elif(point[0] < divisa[0] and point[1] > divisa[1]):
            print("NO")
        elif(point[0] < divisa[0] and point[1] < divisa[1]):
            print("SO")
        elif(point[0] > divisa[0] and point[1] > divisa[1]):
            print("NE")
        elif(point[0] > divisa[0] and point[1] < divisa[1]):
            print("SE")