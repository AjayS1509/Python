# data=[10,20,30,40,50]
#  Expected:----------
# res="10-20-30-40-50

def main():
    data=[10,20,30,40,50]
    print("-".join([str(i) for i in data]))

main()
