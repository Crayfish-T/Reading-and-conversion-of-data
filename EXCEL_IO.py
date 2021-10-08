#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import pandas as pd
import xlrd
import xlwt
from datetime import date,datetime   #表示从大的datetime中调用data,datetime


def read_excel():

  # 打开文件
  data = xlrd.open_workbook('test.xlsx')

  # 获取第一个sheet名称并打印
  sheet1_name = data.sheet_names()[0]
  print(sheet1_name)

  #根据sheet索引或者名称获取sheet内容，同时获取sheet名称、列数、行数
  sheet1 = data.sheet_by_index(0)
  sheet1 = data.sheet_by_name('Sheet1')    # 和上一行等价
  print('sheet1名称:{}\nsheet1列数: {}\nsheet1行数: {}'.format(sheet1.name, sheet1.ncols, sheet1.nrows))

  # 根据sheet名称获取整行和整列的值
  print(sheet1.row_values(0))  
  print(sheet1.col_values(0)) 

  # 获取指定单元格的内容
  print(sheet1.cell(1,0).value)  # 第2行第1列内容：21
  print(sheet1.cell_value(1,0))  # 第2行第1列内容：21
  print(sheet1.row(1)[0].value)  # 第2行第1列内容：21

  # 获取单元格内容的数据类型
  print(sheet1.cell(1,0).ctype)  # 第2行1列内容 
  # 说明：ctype : [0 empty],[1 string], [2 number], [3 date], [4 boolean], [5 error]

  # 获取第1行的数据，获取第1行从第2列到第3列的数据
  print(sheet1.row_values(rowx = 0))
  a = sheet1.row_values(rowx = 0, start_colx = 1, end_colx = 3)
  print(sheet1.row_values(rowx = 0, start_colx = 1, end_colx = 3))

  # 获取第1列的数据，获取第1列从第2行到第3行的数据
  print(sheet1.col_values(colx = 0))
  b = sheet1.col_values(colx = 0, start_rowx = 1, end_rowx = 3)
  print(sheet1.col_values(colx = 0, start_rowx = 1, end_rowx = 3))

  # 获取第3行的长度
  print(sheet1.row_len(rowx=2))



def write_excel(R, C, list1):  # R、C为待写入数据的行数和列数,list1为写入的列表
  workbook = xlwt.Workbook('add_web.xlsx')
  sheet1 = workbook.add_sheet('Sheet1')
  row_num = 0
  for i in range(R):
    col_num = 0
    for j in range(C):
      sheet1.write(row_num,col_num,list1[i][j])
      col_num += 1
    row_num += 1
  workbook.save('add_web.xlsx')




def write_csv():
	data = xlrd.open_workbook('test.xlsx')
	sheet1 = data.sheet_by_index(0)
	a = [1,2,3,4]
	b = [5,6,7,8]
	dataframe = pd.DataFrame({'one':a,'two':b})
	dataframe.to_csv("test.csv",index=False,sep=',')
	print('写入成功')

def read_csv():

	# 打印全部数据
	newdata = pd.read_csv('test.csv')
	print(type(newdata), '\n', newdata, '\n')
	L = []

	with open('test.csv', 'r') as f:
		reader = csv.reader(f)
		print(type(reader))     # 读取为一个对象，后续进行行列操作

		print('\n')

		for row in reader:      # 打印行，第一次会打印列标签
			print('row', row)
			L.append(row)

		print(L)
		print('\n')
		for col in reader:      # 打印列，会打印行标签
			print('col', col)

		header_row = next(reader)
		datas = []
		for row in reader:
			print(row[2])

		# print('\n')
		# result = list(reader)   # 打印第一行
		# print('row0', result[0])


 
if __name__ == '__main__':
 
   # read_excel()
   write_csv()
   read_csv()