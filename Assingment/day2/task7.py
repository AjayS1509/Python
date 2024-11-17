# Task7.1:
# ========
#  Given:--------
#  num=4503
#  PRoblem:----------
# >> using dictionary
#  Expected:------------
#  four five zero three
#  Task7.2:----------
# Given="eight-zero-one-four"
#  Expected:------------
#  8014

num_to_word = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

def main():
    s = ""
    num=4503
    # for ele in str(num):
    #     num_to_word[int(ele)]

    res = " ".join([num_to_word[int(ele)] for ele in str(num)])
    print(res)

    def get_value(val):
        for key,value in num_to_word.items():
            if(value == val):
                return key
        return ''

    num2 = "eight-zero-one-four"
    # for i in num2.split("-"):
    res2 = "".join([str(get_value(ele)) for ele in num2.split("-")])
    print(res2)

    

main()