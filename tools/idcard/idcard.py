# ！/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def check_id_card(id_card_num):

    # reference: 
    # https://baike.baidu.com/item/%E8%BA%AB%E4%BB%BD%E8%AF%81%E6%A0%A1%E9%AA%8C%E7%A0%81/3800388?fr=aladdin
    # https://www.cnblogs.com/xudong-bupt/p/3293838.html

# 校验码计算步骤

# (1)十七位数字本体码加权求和公式 
# 　　S = Sum(Ai * Wi), i = 0, ... , 16 ，先对前17位数字的权求和 
# 　　Ai:表示第i位置上的身份证号码数字值(0~9) 
# 　　Wi:7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 （表示第i位置上的加权因子）
# (2)计算模 
# 　　Y = mod(S, 11)

# (3)根据模，查找得到对应的校验码 
# 　　Y: 0 1 2 3 4 5 6 7 8 9 10 
# 　　校验码: 1 0 X 9 8 7 6 5 4 3 2
 
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


def check(text):
    # pattern = re.compile("(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$")
    pattern = re.compile(r"\d{17}[\d|x|X]")
    result = re.findall(pattern,text) 

    for id_card in result:
        if check_id_card(id_card):
            print(id_card)


if __name__ == "__main__":
    text = ' 330719196804253672孙美洪,330719196804253671孙民华,330702197108020812孙其绥\
    ,330721197010040515孙强飞,33072419770516031X孙群领,330722196501292110孙士儒,330\
    71919610920021X孙世银,33022119670222791X孙树明,330719196104050216孙韬,330721197\
    403162417孙伟戟,A3072519610822411X孙锡华,330724194910022916孙霞,330702197601286\
    024孙献明,330725196303060430孙向波,330724197010122923孙晓红,330724198107250731孙\
    晓明,330721198012040257孙修魁,330325197207044433孙徐胤,320502197812092024孙学军,\
    330183198101251116陈向东,330724196201110015陈向东,330724197110130410错误的身份证\
    号码：330713196804253671330702197108220812、330721197010044515、330724197705660\
    31X、330722196501212110'

    check(text)