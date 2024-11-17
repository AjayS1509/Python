# Given:--------
# data = "ravi-blr-math=50,sci=40,soc=30"
#  Problem:----------
#  >> find the total from the above data
#  Expected:----------
# Total marks = 120


def main():
    data = "ravi-blr-math=50,sci=40,soc=30"
    
    # part = data.split("-",2)
    # t = part[2].split(",")
    # t2 = [int(i.split("=")[-1]) for i in t]
    # print("Total marks = ",sum(t2))
    
    total_marks = [int(i.split("=")[-1]) for i in data.split("-",2)[2].split(",")]
    print("Total marks = ",sum(total_marks))

main()