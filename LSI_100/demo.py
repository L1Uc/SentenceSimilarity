#encoding=utf-8

from Segment import *
from fileObject import FileObj
from sentenceSimilarity import SentenceSimilarity
from sentence import Sentence
from time import clock

if __name__ == '__main__':
    start = clock()
    
    for num in range(1,81):
    
        # 读入后半部分语料
        file_obj = FileObj("sentence2_" + str(num) +".txt")
        train_sentences = file_obj.read_lines()

        # 读入前半部分语料
        file_obj = FileObj("sentence1_" + str(num) +".txt")
        test1_sentences = file_obj.read_lines()


        # 分词工具，基于jieba分词，加了一次封装，主要是去除停用词
        seg = Seg()

        # 生成模型
        ss = SentenceSimilarity(seg)
        ss.set_sentences(train_sentences)
        #ss.TfidfModel()         # tfidf模型
        ss.LsiModel()         # lsi模型
        #ss.LdaModel()         # lda模型

        
        # 计算句子相似度    
        # mysims = ss.mysimilarity(test1_sentences[0])
        # sort_sims = sorted(enumerate(mysims),key = lambda item : -item[1])
        # chosen_sims = sort_sims[:5]
        # for j in range(0,5):
            # print str(chosen_sims[j][0]) + " score:" + str(chosen_sims[j][1])
        
        mysims = ss.mysimilarity(test1_sentences[0])
        sort_sims = sorted(enumerate(mysims),key = lambda item : -item[1])
        chosen_sims = sort_sims[0]
        print str(chosen_sims[0]) + " score:" + str(chosen_sims[1])
        
    finish = clock()
    print "time is: ",(finish - start)," seconds"