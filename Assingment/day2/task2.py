#  names = ["ravi", "arun", "raja", "amit", "Ankur", "hari"]
#  Problem:----------
#  >>filter out names starting with "a"
#  >>Ignore the case
#  >>Store the resultant in a new list
#  Expected:------------
# res = ["arun", "amit", "Ankur"]

def main():
    names = ["ravi", "arun", "raja", "amit", "Ankur", "hari"]
    final_list_with_a = [i for i in names if(i[0].lower() == 'a')]
    print(final_list_with_a)

main()