# Write a Python program to compute element-wise sum of given tuples, using
#  “zip()” function

#  Original tuples:
# (1, 2, 3, 4)
#  (3, 5, 2, 1)
#  (2, 2, 3, 1)
#  Element-wise sum of the said tuples:
#  (6, 9, 8, 6)

def main():
    l = [(1, 2, 3, 4),
    (3, 5, 2, 1),
    (2, 2, 3, 1)]
    result = tuple(sum(values) for values in zip(*l))
    print(result)


main()