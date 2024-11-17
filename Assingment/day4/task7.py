# Define a simple "spelling correction" function correct ()
#  that takes a string and sees to it that
#  1)two or more occurrences of the space character is compressed into one, and
#  2)inserts an extra space after a period if the period is
#  directly followed by a letter.
#  e.g. correct ("This is very funny and cool.Indeed!") should return
#  "This is very funny and cool. Indeed!"

import re

def correct(text):
    # Step 1: Replace two or more spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)
    
    # Step 2: Insert a space after a period if not already followed by a space
    text = re.sub(r'\.(\S)', r'. \1', text)
    
    return text
res = correct ("This is very funny and cool.Indeed!")
print(res)