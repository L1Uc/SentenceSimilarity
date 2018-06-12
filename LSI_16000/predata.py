# -*- coding: utf-8 -*-

import re
import sys
import os,glob

sentence1_log = []
sentence2_log = []
label_log = []

def save_to_file(sentence1_log,sentence2_log,label_log):
    filename_1 = r"sentence1.txt"
    filename_2 = r"sentence2.txt"
    filename_3 = r"label_lc.txt"
    f1 = open(filename_1,"w")
    f2 = open(filename_2,"w")
    f3 = open(filename_3,"w")
    #f1.write('\n'.join(sentence1_log))
    #f2.writelines(sentence2_log)
    for line in sentence1_log:
        f1.write(line+'\n')
    for line in sentence2_log:
        f2.write(line)
    for line in label_log:
        f3.write(line+'\n')
    f1.close()
    f2.close()
    f3.close()
	
def process(filename):
    file = open(filename,"r")
    for eachline in file.readlines():
        mylist = eachline.split('\t',2)
        global sentence1_log
        global sentence2_log
        global label_log
        label_log.append(mylist[0])
        sentence1_log.append(mylist[1])
        sentence2_log.append(mylist[2])

        save_to_file(sentence1_log,sentence2_log,label_log)

if __name__ == "__main__":
    fn = "data_lc.txt"
    process(fn)