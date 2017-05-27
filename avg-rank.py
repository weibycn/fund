# !/usr/bin/python 
# -*- coding: utf-8 -*-
import glob
import sys
	
# 是否已在list中
def get_index(fund_code, all_fund_list):
	fund_num = len(all_fund_list)
	fund_index = 0
	while fund_index < fund_num:
		if fund_code in all_fund_list[fund_index]:
			break;
		fund_index += 1
	
	return fund_index

def main():
		
	# 1、读取所有的结果文件
	result_files = glob.glob('result_*.txt')
	if (len(result_files) == 0) :
		print 'no result file to process!'
		sys.exit(1)
	
	# 将结果都放到一个list中 计算哪个fund 平均排名最高
	# code name type rank1 rate1 rank2 rate2 ... rankn raten average_rank
	
	file_num = 0
	all_fund_list = []
	
	# 循环处理文件
	for filename in result_files:
		print 'process file:\t' + str(file_num) + '\t' + filename
		file_object = open(filename, 'r')
		try:
			# 第1行 表头不处理 从第2行开始处理
			file_object.readline()
			while 1:
				funds_txt = file_object.readline()
				if not funds_txt:
					break;
					
				# 转成list
				fund = funds_txt.split()
				
				# 如果是第1个文件 直接append
				if 0 == file_num:
					fund_list= []
					fund_list.append(fund[1])
					fund_list.append(fund[2])
					fund_list.append(fund[3])
					fund_list.append(fund[0])
					fund_list.append(fund[7])
					
					all_fund_list.append(fund_list)
				else:
					# 查找是否已在list中
					fund_num = len(all_fund_list)
					fund_index = get_index(fund[1], all_fund_list)
					if fund_index < fund_num:
						# list中已存在 只append rank 和 rate
						#print fund_code + '\t' + str(fund_index) + '\t' + str(all_fund_list[fund_index])
						all_fund_list[fund_index].append(fund[0])
						all_fund_list[fund_index].append(fund[7])
					else:
						# 如果不存在 不仅需要将其加入list中 同样需要将其他几个 rank 和 rate 补上
						# 如果本fundcode在前几个文件中不存在 就是倒数第一 第100名吧 rank 默认100 rate 默认0
						#print fund_code + '\tnot found!'
						fund_list= []
						# code name type
						fund_list.append(fund[1])
						fund_list.append(fund[2])
						fund_list.append(fund[3])
						# 补上 前几个文件的 rank 和 rate
						for i in range(file_num):
							fund_list.append('100')
							fund_list.append('0')
						# 加上当前的rank 和 rate
						fund_list.append(fund[0])
						fund_list.append(fund[7])
						
						#将其加入列表
						all_fund_list.append(fund_list)						
						
		finally:
			file_object.close()
		
		# 还有 从第2个文件开始 如果有fund 不在本文件中出现 就是倒数第一 第100名吧 还要将rank 和 rate 补上 擦 挺复杂
		if file_num > 0:
			# 最长的len 为 5 + 2 * file_num
			fund_len = 5 + 2 * file_num
			fund_num = len(all_fund_list)
			fund_index = 0
			while fund_index < fund_num:
				if len(all_fund_list[fund_index]) < fund_len:
					all_fund_list[fund_index].append('100')
					all_fund_list[fund_index].append('0')
				
				fund_index +=1
		
		# 处理下一个文件
		file_num += 1
	
	'''
	print 'filenum:' + str(file_num)
	print len(all_fund_list)
	for fund_list in all_fund_list:
		print fund_list
	'''
	
	# 2、计算平均排名
	fund_num = len(all_fund_list)
	fund_index = 0
	while fund_index < fund_num:
		sum_rank = 0
		# 有几个文件 就有几个排名 rank的index 3 5 7 ... ...
		for i in range(file_num):
			sum_rank += int(all_fund_list[fund_index][3 + 2 * i])
			
		# 计算平均排名
		avg_rank = float('%.2f' %(float(sum_rank) / file_num))
	
		# 加入avg_rank
		all_fund_list[fund_index].append(avg_rank)
		
		# 处理下一个
		fund_index +=1
		
	# 3、排序 写文件 打印
	# avg_rank的index 5 + 2 * file_num
	all_fund_list.sort(key=lambda fund: fund[3 + 2 * file_num])
	
	file_object = open('results.txt', 'w')
	int_rank = 1
	try:
		for fund_list in all_fund_list:
			print str(int_rank) + '\t' + '\t'.join('{0}'.format(n) for n in fund_list)
			file_object.write(str(int_rank) + '\t' + '\t'.join('{0}'.format(n) for n in fund_list) + '\n')
			int_rank += 1
	finally:
			file_object.close()
	
	
	sys.exit(0)

def test():
	all_fund_list = []
	
	file_object = open('test.txt', 'r')
	try:
		file_object.readline()
		while 1:
			funds_txt = file_object.readline()
			if not funds_txt:
				break;
				
			fund = funds_txt.split()
			#print fund[2] + '\t' + fund[3]
			fund_list= []
			fund_list.append(fund[1])
			fund_list.append(fund[2])
			fund_list.append(fund[3])
			fund_list.append(fund[0])
			fund_list.append(fund[7])
			
			all_fund_list.append(fund_list)
	finally:
		file_object.close()

	fund_code_list = ['150294', '002534', '0004', '502008', '000114']
	fund_num = len(all_fund_list)
	print fund_num
	for fund_code in fund_code_list:
		fund_index = get_index(fund_code, all_fund_list)
		if fund_index < fund_num:
			print fund_code + '\t' + str(fund_index) + '\t' + str(all_fund_list[fund_index])
		else:
			print fund_code + '\tnot found!'
		
	
	print '\n\n\n\n'
	#print all_fund_list.index('150294')

if __name__ == "__main__":	
	#test()
	main()

	
