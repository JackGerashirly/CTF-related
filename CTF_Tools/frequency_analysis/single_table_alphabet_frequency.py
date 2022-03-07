# -*- coding:utf-8 -*-
from __future__ import division  # 导入精确除法模块

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


# Tokenize the Book
words = tokenize()

# Get Word Count
sum = 0
frequency_list = []
for i in range(0, 26):
    word = 'a'
    word = chr(ord(word) + i)
    frequency = count_word(words, word)
    frequency_list.append(frequency)
    sum += frequency

# Print frequency
for i in range(0, 26):
    word = "a"
    print('Word: [' + chr(ord(word) + i) + '] Frequency: ', (frequency_list[i] * 100 / sum))
# Frequency Table Reference: http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html

