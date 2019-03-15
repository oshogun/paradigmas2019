# -*- coding: utf-8 -*-

n = int(input())

experiments = [None, None] * n 
animals = [['C', 0], ['R', 0], ['S', 0]]

for i in range(0, n):
	experiments[i] = input().split()
	experiments[i][0] = int(experiments[i][0])	

totalAnimalCount = 0


for i in range(0,n):
	totalAnimalCount = totalAnimalCount + experiments[i][0]
	if experiments[i][1] == 'C':
		animals[0][1] += experiments[i][0]
	elif experiments[i][1] == 'R':
		animals[1][1] += experiments[i][0]
	elif experiments[i][1] == 'S':
		animals[2][1] += experiments[i][0]

percentRabbit = (animals[0][1] / totalAnimalCount) * 100
percentMickey = (animals[1][1] / totalAnimalCount) * 100
percentFroggo = (animals[2][1] / totalAnimalCount) * 100

print('Total: ' + str(totalAnimalCount) + ' cobaias')

print('Total de coelhos: ' + str(animals[0][1]))
print('Total de ratos: ' + str(animals[1][1]))
print('Total de sapos: ' + str(animals[2][1]))

print('Percentual de coelhos: %.2f' %(percentRabbit))
print('Percentual de ratos: %.2f' %(percentMickey))
print('Percentual de sapos: %.2f' %(percentFroggo))




