##############################################
# File name: question2.py                    #
# Author: Eugene de Beste                    #
# Email: eugene.debeste@voss-solutions.com   #
# Title: Anagram Determination               #
##############################################

# "An anagram is a type of word play, the result of rearranging 
# the letters of a word or phrase to produce a new word or phrase,
# using all the original letters exactly once." - Wikipedia

# Below is a bad implementation of determining whether a word,
# given another word, is an anagram. Your task is to optimize this
# implementation in terms of code lines. Assume case is irrelevant.

original = "torch wood"
toCheck = "doctor who"


def isAnagram(word1, word2):
    final_word2 = ""
    continue_loop = True
    for letter1 in word1:
        if continue_loop:
            continue_loop = False
            counter = 0
            for letter2 in word2:
                counter += 1
                if letter1 == letter2:
                    word2 = word2.replace(letter2, '', 1)
                    word1 = word1.replace(letter2, '', 1)
                    final_word2 += letter2
                    continue_loop = True
                    break
        else:
            return -1
            break
    if word1 or word2:
        return -1
    return 1

result = isAnagram(original, toCheck)
if result == 1:
    print "This is an anagram"
elif result == -1:
    print "This is not an anagram"

