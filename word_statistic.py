#!/usr/bin/env python
# coding=utf-8


import string 
import csv

class wordStatistic:
    # 该类只对外提供Statistic方法和prettyPrint方法
    # 以及保存csv文件的方法
    __stop_word = open("../DataAnalysisTraining/StopWordsList.txt").read()
    def __init__(self, fpath):
        self.__word_tbl = {}
        self.__file_pth = open(fpath, "r")
        self.__file_str = self.__file_pth.read()
        self.__proc_flg = 0
    
    def __addWord(self, word, wcDict):
        ''' Update the word frequency '''
        if word in wcDict:
            wcDict[word] += 1
        else:        
            wcDict[word] = 1

    def __processLine(self, line, wcDict):
        # 去掉首尾空格然后用空格分割一下
        wordList = line.strip().split()
        for word in wordList:
            if word == '--':
                continue
            word = word.lower().strip().strip(string.punctuation)
            # 加入停用词(StopWord)优化输出结果
            if word in self.__stop_word:
                continue
            self.__addWord(word, wcDict)
        self.__proc_flg = 1

    def Statistic(self):
        # 检测文件路径
        # 进行文件内容统计，返回一个字典
        if self.__proc_flg == 0:
            self.__processLine(self.__file_str, self.__word_tbl)
        return self.__word_tbl
    
    def prettyPrint(self):
        # 按照表格输出文件内容统计信息
        if self.__proc_flg == 0:
            self.__processLine(self.__file_str, self.__word_tbl)

        wcDict = self.__word_tbl
        valKeyList = []
        for key,val in wcDict.items():
            valKeyList.append((val, key))

        valKeyList.sort(reverse=True)
        
        print "%-10s%-10s" % ('Word', 'Count')
        print '-'*21
        for val,key in valKeyList:
            print "%-12s  %3d" % (key, val)
        # print self.__stop_word
    
    def save_csv(self, file_info):
        if self.__proc_flg == 0:
            self.__processLine(self.__file_str, self.__word_tbl)
        if file_info[-4] != '.':
            file_info = file_info + ".csv"
        
        fp = open(file_info, "w")

        wcDict = self.__word_tbl
        valKeyList = []
        for key,val in wcDict.items():
            valKeyList.append((val, key))

        valKeyList.sort(reverse=True)
        # python格式化字符串
        fp.write("Word,Count\n")
        for val,key in valKeyList:
            print key
            fp.write('{key},{val}\n'.format(key=key, val=val))
        fp.close()

