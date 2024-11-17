# Write program to find the most repeated word in a file
#  Assume the file "data.txt" contains----------------------------------
# this that this this this that
#  then that that that
#  that this then that
#  Expected:----------
# Most repeated word in the file is = this

from collections import Counter

with open('data.txt','r') as file:
    words = file.read().split()
    print(words)

word_counts = Counter(words)
print(word_counts)

most_common_word,count = word_counts.most_common()[0]

print(most_common_word)