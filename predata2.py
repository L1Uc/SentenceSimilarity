# -*- coding: utf-8 -*-

import re
import sys
import os,glob

sentence1_log = []
sentence2_log = []
id_group = 1

def save_to_file(sentence1_i_log,sentence2_i_log,id_group):
	filename_1 = r"sentence1_" + str(id_group) + ".txt"
	filename_2 = r"sentence2_" + str(id_group) + ".txt"
	f1 = open(filename_1,"w")
	f2 = open(filename_2,"w")
	#f1.write('\n'.join(sentence1_log))
	#f2.writelines(sentence2_log)
	for line in sentence1_i_log:
		f1.write(line+'\n')
	for line in sentence2_i_log:
		f2.write(line)
	f1.close()
	f2.close()
	
def process(filename):
	file = open(filename,"r")
	for eachline in file.readlines():
		mylist = eachline.split('\t',2)
		
		global sentence1_log
		global sentence2_log
		global id_group
		
		sentence1_log.append(mylist[1])
		sentence2_log.append(mylist[2])
		

if __name__ == "__main__":
	fn = "data_lc.txt"
	process(fn)
	for id_group in range(1,81):
		sentence1_i_log = sentence1_log[(id_group-1)*100:id_group*100]
		sentence2_i_log = sentence2_log[(id_group-1)*100:id_group*100]
		save_to_file(sentence1_i_log,sentence2_i_log,id_group)
	
	
	
	
	
	
