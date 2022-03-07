# -*- coding:utf-8 -*-

file = open('a.txt', 'r')
book = file.read()


def tokenize():
    if book is not None:
        words = book.lower().split()
        return words
    else:
        return None


def count_word(tokens, token):
    count = 0

    for element in tokens:
        # Remove Punctuation
        word = element.replace(",", "")
        word = word.replace(".", "")

        # Found Word?
        if word == token:
            count += 1
    return count


# Tokenize the Book
words = tokenize()

# Get Word Count
word = raw_input("需要统计的单词：")  # 或者直接赋值 word = 'soon'
frequency = count_word(words, word)
print('Word: [' + word + '] Frequency: ' + str(frequency))