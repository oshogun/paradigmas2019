alternatives = ['A', 'B', 'C', 'D', 'E']
while True:
    testCases = int(input())
    if testCases == 0:
        break
    for i in range(0, testCases):
        answer = input().split()
        trueCount = 0
        for i in range(0, 5):
            answer[i] = int(answer[i])
            if answer[i] > 127:
                answer[i] = False 
            else:
                answer[i] = True
                trueCount += 1
        
        if trueCount == 1:
            for i in range(0, 5):
                if answer[i] == True:
                    print(alternatives[i])
        else:
            print('*')