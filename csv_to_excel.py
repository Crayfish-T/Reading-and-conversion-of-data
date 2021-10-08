#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import pandas as pd
import xlrd
import xlwt

inputname = 'input_data.csv'
outputname = 'output.xls'




with open(inputname,'r',encoding='utf8') as fp1:
	list1 = [i for i in csv.reader(fp1)]

row = len(list1)
col = len(list1[0])
print('行列数分别为',row,col)

def write_excel(R, C, list1):  # R、C为待写入数据的行数和列数,list1为写入的列表
  
  workbook = xlwt.Workbook(outputname)
  sheet1 = workbook.add_sheet('Sheet1')
  row_num = 0
  for i in range(R):
    col_num = 0
    for j in range(C):
      sheet1.write(row_num,col_num,list1[i][j])
      col_num += 1
    row_num += 1
  workbook.save(outputname)

write_excel(row, col, list1)
print('转换完成')