while True:
    testCase = input().split()

    testCase[0] = int(testCase[0])
    testCase[1] = int(testCase[1])
    testCase[2] = int(testCase[2])
    testCase[3] = int(testCase[3])

    if(testCase == [0,0,0,0]):
        break
    
    currentMinutes = testCase[0] * 60 + testCase[1]
    alarmMinutes = testCase[2] * 60 + testCase[3]
    if (currentMinutes > alarmMinutes):
        alarmMinutes += 1440
    sleepLeft = alarmMinutes - currentMinutes
    
    print(sleepLeft)
