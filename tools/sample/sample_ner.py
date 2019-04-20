#!/usr/bin/env python
# coding=UTF-8
'''
@Description: NER子类例子，新工程可参考此文件
@Author: ansvver(ansvver.cn@gmail.com)
@Date: 2019-04-20 16:00:36
@LastEditTime: 2019-04-20 16:58:14
'''

from tools.ner_tool import NERTool
from tools.ner_tool import Entity
from typing import List
import re


class SampleNERTool(NERTool):
    def __init__(self):
        super(SampleNERTool, self).__init__()
        self.tag = "SAMPLE"
        self.sample_patt = re.compile('(谁|为什么|怎么)')

    def ner(self, inputs):
        ret = []
        for input in inputs:
            ent_list = []
            for item in self.sample_patt.finditer(input):
                ent = Entity()
                ent.tag = self.tag
                ent.word = item.group()
                ent.start = item.span()[0]
                ent.end = item.span()[1]
                ent_list.append(ent)
            ret.append(ent_list)
        return ret


def _test():
    st = SampleNERTool()
    inputs = ['谁干的？', '为什么会这样？是谁?', '怎么做的？']
    for res in st.ner(inputs):
        print('-------')
        for ent in res:
            print(ent)


if __name__ == "__main__":
    _test()
