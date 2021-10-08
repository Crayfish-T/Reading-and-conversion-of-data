#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import xlrd

inputname = 'input_data.xls'
outputname = 'output.csv'


data = xlrd.open_workbook(inputname)
sheet1 = data.sheet_by_index(0)
output = open(outputname, 'w', newline = '',encoding='utf8')
writer = csv.writer(output)

print('sheet1名称:{}\nsheet1列数: {}\nsheet1行数: {}'.format(sheet1.name, sheet1.ncols, sheet1.nrows))
Len = sheet1.nrows
print('共有',Len,'行')

n = 0
for i in range(Len):
	n += 1
	a = sheet1.row_values(i)
	print(a)
	writer.writerow(a)
	print(n,'行已完成写入')

