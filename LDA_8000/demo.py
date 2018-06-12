#encoding=utf-8

from Segment import *
from fileObject import FileObj
from sentenceSimilarity import SentenceSimilarity
from sentence import Sentence
from time import clock

if __name__ == '__main__':
    start = clock()
    
    # 读入后半部分语料
    file_obj = FileObj(r"sentence2.txt")
    train_sentences = file_obj.read_lines()

    # 读入前半部分语料
    file_obj = FileObj(r"sentence1.txt")
    test1_sentences = file_obj.read_lines()


    # 分词工具，基于jieba分词，加了一次封装，主要是去除停用词
    seg = Seg()

    # 生成模型
    ss = SentenceSimilarity(seg)
    ss.set_sentences(train_sentences)
    #ss.TfidfModel()         # tfidf模型
    #ss.LsiModel()         # lsi模型
    ss.LdaModel()         # lda模型

    
    # 计算句子相似度    
    # for i in range(0,len(train_sentences)/100):
        # mysims = ss.mysimilarity(test1_sentences[i*100])
        # # 每一百行为一个整体
        # sims_divided = mysims[i*100:(i+1)*100]
        # # 对一百行内的相似度进行排序
        # sort_sims = sorted(enumerate(sims_divided),key = lambda item : -item[1])
        # # 选择前五个最高的相似度进行输出
        # chosen_sims = sort_sims[:5]
        # for j in range(0,5):
            # print str(chosen_sims[j][0]) + " score:" + str(chosen_sims[j][1])
    
    for i in range(0,len(train_sentences)/100):
        mysims = ss.mysimilarity(test1_sentences[i*100])
        # 每一百行为一个整体
        sims_divided = mysims[i*100:(i+1)*100]
        # 对一百行内的相似度进行排序
        sort_sims = sorted(enumerate(sims_divided),key = lambda item : -item[1])
        # 选择相似度最高的进行输出
        chosen_sims = sort_sims[0]
        print str(chosen_sims[0]) + " score:" + str(chosen_sims[1])
    
    finish = clock()
    print "time is: ",(finish - start)," seconds"