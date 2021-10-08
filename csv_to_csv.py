#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

inputname = 'input_data.csv'
outputname = 'output.csv'


with open(inputname,'r',encoding='utf8') as fp1:
	list1 = [i for i in csv.reader(fp1)]
# print(len(list1))

output = open(outputname, 'w', newline = '',encoding='utf8')
writer = csv.writer(output)

for i in range(322040):
	for j in range(23):
		if list1[i][j] == '●':
			list1[i][j] = list1[i][7]
		elif list1[i][j] == '-':
			list1[i][j] = 0
		else:
			pass
	writer.writerow(list1[i])
	print(list1[i])

