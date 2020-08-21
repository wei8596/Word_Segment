# -*- coding: UTF-8 -*-

"""
Author:范真瑋
Date:2020/08/14
Word Segmentation
"""


# Reverse Maximum Match Method (RMM)
class RMM(object):
    def __init__(self, dictPath):
        self.dictionary = set()
        self.maxDict = 0
        # read dictionary
        with open(dictPath, 'r', encoding='utf8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line) > self.maxDict:
                    self.maxDict = len(line)

    # segmentation
    def segment(self, text):
        wordList = []
        index = len(text)
        while index > 0:
            word = None
            for size in range(self.maxDict, 0, -1):
                if index - size < 0:
                    continue
                segment = text[(index - size):index]
                # in the dictionary
                if segment in self.dictionary:
                    word = segment
                    wordList.append(word)
                    index -= size
                    break
            # not in the dictionary
            if word is None:
                wordList.append(segment)
                index -= 1
        # reverse list
        return wordList[::-1]


if __name__ == '__main__':
    dictPath = 'dict_no_space.txt'

    # input text
    inputText = input('input:')
    rmm = RMM(dictPath=dictPath)
    result = rmm.segment(text=inputText)
    # 2 output formats
    print(result)
    # print("/".join(i for i in result))
