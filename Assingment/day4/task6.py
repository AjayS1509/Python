#  Write a function filter_long_words() that takes a list of words and an integer n
#  and returns the list of words that are longer than n
def filter_long_words(words,n):
    return [ele for ele in words if(len(ele) >= n)]

def main():
    n = 6
    words = ["apple", "banana", "strawberry", "grape"]

    res = filter_long_words(words,n)
    print(*res)

main()