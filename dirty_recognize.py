"""
@function:实现脏数据的识别
@author: ZhuJianhao
@contact: zjmac1635@163.com
@time: 2021/7/29 
"""

from trie import Trie


class dirty_reg(object):
    
    def __init__(self, path):
        self.obj = Trie()#该类有一个实例化对象trie
        self.build(path)
        
    def insert_new(self, word_list):
        word_list = [word.lower() for word in word_list]
        self.obj.insert(word_list)

    def build(self, path):
        f = open(path, "r", encoding="utf-8")
        for line in f:
            line = line.strip()
            if line:
                self.insert_new(line)

    def enumerateMatchList(self, word_list):
        word_list = [word.lower() for word in word_list]
        match_list = self.obj.enumerateMatch(word_list)
        return match_list

    def match(self, query):
        al = set()
        length = 0
        for indx in range(len(query)):
            index = indx + length
            match_list = self.enumerateMatchList(query[index:])
            if match_list == []:
                continue
            else:
                match_list = max(match_list)
                length = len("".join(match_list))
                al.add(match_list)
        return al