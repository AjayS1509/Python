#  cities = ["blr", "chn", "mum", "hyd", "del"]
#  grps = ["blr", "del", "noida"]
#  Problem:----------
#  >>find the common city names between two lists
#  >>Don't use set operations
#  Expected:------------
#  common = ["blr", "del"]

def main():
    cities = ["blr", "chn", "mum", "hyd", "del"]
    grps = ["blr", "del", "noida"]
    final = [i  for i in cities if(i in grps)]
    print(final)

main()