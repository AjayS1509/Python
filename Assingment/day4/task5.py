# Write a function find_longest_word() that takes a list of words and returns the
#  length of the longest one.




def main():
    words = ["apple", "banana", "strawberry", "grape"]
    lon = 0
    lon_word = ''
    for ele in words:
        if(len(ele) > lon):
            lon = len(ele)
            lon_word = ele
        
    print("longest length = ",lon)
    print("longest word = ",lon_word)

main()