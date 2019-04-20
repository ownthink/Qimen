#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 工具类身份证号码提取
@Author: ZHANG Tao(zhangtaochn@g126.com)
@Date: 2019-4-20 23:02:19
@LastEditTime: 2019-04-21 00:08:07
'''

from typing import List
import re

class CheckIdCard():


    def __init__(self):
        self.pattern = re.compile(r"\d{17}[\d|x|X]")

    def check_id_card(self, id_card_num):

        check_num = ['1','0','X','9','8','7','6','5','4','3','2']
        id_card_weight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        check_sum = 0
        
        for i in range(17):
            check_sum += int(id_card_num[i])*id_card_weight[i]
        check_mod = check_sum%11

        if check_num[check_mod] == id_card_num[17]:
            return 1
        else:
            return 0
    

    def check(self, text):
        # pattern = re.compile("(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$")
        result = list()

        for id_card in re.findall(self.pattern,text) :
            if self.check_id_card(id_card):
                result.append(id_card)
        return result

            
def _test():
    test_sample = CheckIdCard()
    # inputs = ['谁干的？', '为什么会这样？是谁?', '怎么做的？']

    inputs = ' 330719196804253672孙美洪,330719196804253671孙民华,330702197108020812孙其绥\
    ,330721197010040515孙强飞,33072419770516031X孙群领,330722196501292110孙士儒,330\
    71919610920021X孙世银,33022119670222791X孙树明,330719196104050216孙韬,330721197\
    403162417孙伟戟,A3072519610822411X孙锡华,330724194910022916孙霞,330702197601286\
    024孙献明,330725196303060430孙向波,330724197010122923孙晓红,330724198107250731孙\
    晓明,330721198012040257孙修魁,330325197207044433孙徐胤,320502197812092024孙学军,\
    330183198101251116陈向东,330724196201110015陈向东,330724197110130410错误的身份证\
    号码：330713196804253671330702197108220812、330721197010044515、330724197705660\
    31X、330722196501212110'


    for res in test_sample.check(inputs):

        print(res)

if __name__ == "__main__":
    _test()


