#!/usr/bin/env python
# coding=UTF-8
'''
@Description: NER工具父类
@Author: ansvver(ansvver.cn@gmail.com)
@Date: 2019-04-20 14:06:51
@LastEditTime: 2019-04-20 16:59:05
'''

import sys
import json
from typing import List

# 全局的实体标签字典，key -> 大写字母单词缩写, value -> (中文简短描述, 附加备注信息)
GLOBAL_TAG_DICT = {"SAMPLE": ("示例", "示例例子，后续正式发版可考虑删除")}


class Entity(object):
    """实体类"""

    def __init__(self):
        self._tag = ''  # 大写字母单词缩写, 如"EMAIL"、 "PHONE"等，请在`GLOBAL_TAG_DICT`中注册
        self._word = ''  # 句子中识别出来的名词
        self._start = -1  # Optional, 在句子中的起始下标，注意下标从0开始
        self._end = -1  # Optional, 在句子中的结束下标，注意下标从0开始

    @property
    def tag(self) -> str:
        return self._tag

    @tag.setter
    def tag(self, value: str):
        assert value.upper(
        ) in GLOBAL_TAG_DICT, '请确认tag标签已在`GLOBAL_TAG_DICT`中注册！'
        self._tag = value

    @property
    def word(self) -> str:
        return self._word

    @word.setter
    def word(self, value: str):
        self._word = value

    @property
    def start(self) -> int:
        return self._start

    @start.setter
    def start(self, value: int):
        assert value >= 0, '请确保下标>0'
        self._start = value

    @property
    def end(self) -> int:
        return self._end

    @end.setter
    def end(self, value: int):
        assert value >= 0, '请确保下标>0'
        self._end = value

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)


class NERTool(object):
    """实体识别工具父类"""

    def __init__(self):
        super(NERTool, self).__init__()

    def ner(self, inputs: List[str]) -> List[List[Entity]]:
        """子类需重写此函数, 输入是字符列表，输出是实体列表组成的列表（每个句子对应一个实体列表）"""
        raise NotImplementedError
