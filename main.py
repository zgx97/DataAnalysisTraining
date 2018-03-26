#!/usr/bin/env python
# coding=utf-8

from Model.drawing import DrawingDict 
from Model.word_statistic import wordStatistic

if __name__ == "__main__":
    st = wordStatistic("./DataFile/Gettysburg_Address.txt");
    # print st.Statistic()
    # st.prettyPrint() 
    st.save_csv("./DataFile/data.csv")
    dd = DrawingDict("./DataFile/data.csv")
    dd.drawing("Count")
    