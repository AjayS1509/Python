#  grp1 = ["red=10", "blue=20", "green=30", "black=40"]
#  grp2 = ["orange=50", "brown=45", "red=5", "black=33"]
#  Problem:----------
# >> using set operations- find the common colours b/w them
#  Expected:
# ==========
#  print(res) # {"red", "black"}


def main():
    grp1 = ["red=10", "blue=20", "green=30", "black=40"]
    grp2 = ["orange=50", "brown=45", "red=5", "black=33"]

    res = [i.split("=")[0] for i in grp1 if(i.split("=")[0] in [j.split("=")[0] for j in grp2])]
    print(set(res))

main()