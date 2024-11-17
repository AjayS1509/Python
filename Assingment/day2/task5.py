# Given:--------
#  nums = [1,2,3,4,5]
#  Problem:----------
# >> square each number- INPLACE OPERATION
#  Expected:----------
# print(nums) # [1,4,9,16,25]


def main():
    nums = [1,2,3,4,5]
    print([i*i for i in nums])

main()