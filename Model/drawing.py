#!/usr/bin/env python
# coding=utf-8

'''
传入一个csv文件，根据csv文件绘图
设置异常处理
'''
import pandas as pd

class DrawingDict:
    def __init__(self, csv_path):
        try:
            self.csv_file = pd.read_csv(csv_path)
        except Exception as err:
            print "drawung.py : %s" % err
     
    def __proc_csv(self, key, ascdStat=False, endInd=10):
        self.get_info = self.csv_file.sort_values(key, ascending=False)[:endInd]
    
    def drawing(self, key, ascdStat=False, endInd=10):
        self.__proc_csv(key, ascdStat, endInd)
        print "self.get_info is : \n%s\n" % (self.get_info)
        
        print type(self.get_info)
        # self.get_info["Word"] = unicode(self.get_info["Word"], "utf-8")
        print "%s" % self.get_info["Word"]
        
        try:
            data_plot = self.get_info.plot(kind="bar", x=self.get_info["Word"], title="Words Count Table", legend=False)
        except Exception as err:
            print err
        
        fig = data_plot.get_figure()
        fig.savefig("../StatisticPicture/img.png")

if __name__ == '__main__':
    dd = DrawingDict("../DataFile/data.csv")
    dd.drawing("Count")