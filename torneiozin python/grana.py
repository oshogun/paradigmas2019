# -*- coding: utf-8 -*-

cash = int(input())


moneys = [100, 50, 20, 10, 5, 2, 1]

result = str(cash) + '\n'
for i in range(0, len(moneys)):
	if (cash / moneys[i] != 0):
		result += str(int(cash / moneys[i])) + ' nota(s) de R$ ' + str(moneys[i])+',00\n'
		cash = cash % moneys[i]
	else:
		result +=("0 nota(s) de R$ " + str(moneys[i]) + ",00\n")
print(result, end='')