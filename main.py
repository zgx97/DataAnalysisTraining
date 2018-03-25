#!/usr/bin/env python
# coding=utf-8

from drawing import DrawingDict 
from word_statistic import wordStatistic

if __name__ == "__main__":
    st = wordStatistic("./Gettysburg_Address.txt");
    # print st.Statistic()
    # st.prettyPrint() 
    st.save_csv("./data.csv")
    dd = DrawingDict("./data.csv")
    dd.drawing("Count")
    