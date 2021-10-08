#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
outputname = 'output.csv'

L = []
n = 0
cut = 4
epoch = 0

output = open('test.csv', 'w', newline = '',encoding='utf8')
writer = csv.writer(output)

list1.append('\n')
for x in range(len(list1)):
	if n < cut:
		L.append(list1[epoch*cut+n])
		n += 1
	else:
		epoch += 1
		writer.writerow(L)
		n = 0
		L = []
		L.append(list1[epoch*cut+n])
		n+=1
		