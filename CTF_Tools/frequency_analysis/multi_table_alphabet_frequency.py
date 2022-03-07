# -*- coding:utf-8 -*-
from __future__ import division  # 导入精确除法模块
import re

file = open('a.txt', 'r')  # 需要统计的文本文件
book = file.read()


def tokenize():
    if book is not None:

        # Lower the Alphabet
        words = book.lower()

        # Remove Punctuation and Sign
        for elements in words:
            c = ord(elements)
            if c < 65 or c > 122 or (c > 90 and c <97):
                words = words.replace(elements, "")
        return words

    else:
        return None


def count_word(tokens, token):
    count = 0

    for word in tokens:

        # Found Word
        if word == token:
            count += 1
    return count


# Divide and Get Frequency
def get_frequency(blocksize):

    # Tokenize the Book
    words = tokenize()
    print "Start to Get Blocksize equals", blocksize, "..."

    # Compute the number of blocks
    blocks = words.__len__() // blocksize

    for i in range(0, blocksize):

        wordss = ""

        # Get one of the blocks
        for j in range(0, blocks):
            wordss += words[j * blocksize + i]

        # Print the Temporary Block
        print "\n", "Block", i + 1, ": ", wordss

        # Get Word Count
        sum = 0
        frequency_list = []
        for k in range(0, 26):
            word = 'a'
            word = chr(ord(word) + k)
            frequency = count_word(wordss, word)
            frequency_list.append(frequency)
            sum += frequency

        # Print frequency
        print "\n", "The Result of Block", i + 1, ": "
        for k in range(0, 26):
            word = "a"
            print('Word: [' + chr(ord(word) + k) + '] Frequency: ', (frequency_list[k] * 100 / sum))


get_frequency(12)
print "Frequency  Counting Finish!"
# Frequency Table Reference: http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
# Blocksize 延展到 26 位成为一次一密