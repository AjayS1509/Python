# Given:--------
#  names = ["ravi", "arun", "raja", "amit", "ankur", "harish"]
#  Problem:----------
#  >> Convert the first and last letter to upper case each string
#  Expected:----------
# print(res) # ["RavI", "AruN", "RajA", "AmiT", "AnkuR", "HarisH"]

def main():
    names = ["ravi", "arun", "raja", "amit", "ankur", "harish"]

    res = [name[0].upper()+ name[1:-1].lower()+ name[-1].upper() for name in names]
    print(res)

main()