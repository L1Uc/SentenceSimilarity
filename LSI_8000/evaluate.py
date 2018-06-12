# -*- coding: utf-8 -*-

# import re
# import sys
# import os
# import glob
# import codecs

if __name__ == "__main__":
    correct_id = []
    result_id = []
    count_id = []
    i = -1
    accuracy = 1
    f_label = open("label_lc.txt", "r")
    f_result = open("result_lsi_8000.txt")

    for eachline1 in f_label.readlines():
        i += 1
        if eachline1[0] == "1":
            correct_id.append(str(i))
        else:
            continue

    for eachline2 in f_result.readlines():
        result_list = eachline2.split()
        result_id.append(result_list[0])

    f_label.close()
    f_result.close()

    # 第一行数据处理
    result_id[0] = '0'
    correct_id.insert(0, '0')

    # 将字符串列表转为整型列表
    result_id = map(eval, result_id)
    correct_id = map(eval, correct_id)

    # result_id再处理
    for j in range(0, 80):
        for k in range(0, 5):
            result_id[k+j*5] = result_id[k+j*5] + j*100

    # 取正确率最高的一个句子
    # for j in range(0,80):
    #     result_id[j] = result_id[j] + j*100

    # 得到相同元素及个数
    count_id = [item for item in correct_id if item in result_id]
    print "number of same item: ", len(count_id)

    # 计算准确率
    accuracy = float(len(count_id))/float(400)
    print "accuracy: ", accuracy
    print '\n'

    print "correct_id = ", correct_id
    print '\n'
    print "result_id = ", result_id
    print '\n'
    print "count_id = ", count_id
