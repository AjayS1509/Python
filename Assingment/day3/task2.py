#  Define a procedure histogram() that takes a list of integers and prints a histogram
#  to the screen. For example, histogram([4, 9, 7]) should print the following:
#  ****
#  *********
#  *******

def histogram(list_data):
    for ele in list_data:
        print("".join([str('*') for i in range(ele)]))
    

def main():
    data = [4, 9, 7]
    histogram(data)

main()