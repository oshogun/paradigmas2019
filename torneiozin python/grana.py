# -*- coding: utf-8 -*-

cash = int(input())

moneys = [100, 50, 20, 10, 5, 2, 1]

for i in range(0, len(moneys)):
	if (cash / moneys[i] != 0):
		print(str(int(cash / moneys[i])) + ' nota(s) de ' + str(moneys[i])+',00')
		cash = cash % moneys[i]