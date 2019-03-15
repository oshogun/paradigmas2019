granas = [50, 10, 5, 1]
numTests = 1

while True:
    saque = int(input())
    if saque == 0:
        break 
   
    output = [0, 0, 0, 0]

    for i in range(0, 4):
        if i < 3:
            output[i] = str(int(saque / granas[i])) + ' '
        else:
            output[i] = str(int(saque / granas[i]))
        saque %= granas[i]

    print("Teste " + str(numTests))
    print(''.join(output)+ '\n')
    numTests += 1