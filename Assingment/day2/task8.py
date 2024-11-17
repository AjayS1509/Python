# grps = ["alpha", "beta", "delta", "alpha", "beta", "omega","alpha"]
#  Problem:----------
#  find the unique & duplicate values in above list
#  Expected:----------
# print(unique)
#  # ["delta", "omega"]
#  print(duplicates) # ["alpha", "beta"]


def main():
    grps = ["alpha", "beta", "delta", "alpha", "beta", "omega","alpha"]

    data_unique_list = list(set(grps))
    data_unique = []
    data_duplicates = []
    for ele in data_unique_list:
        if(grps.count(ele) == 1):
            data_unique.append(ele)
        else:
            data_duplicates.append(ele)
    print(data_unique)
    print(data_duplicates)



main()