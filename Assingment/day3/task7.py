#  Write a Python program to count the elements in a list until an element is a tuple.
#  Sample input : list = [10, 20, 30, (40,50), 60]
#  Sample output = 3

def main():
    list_data = [10, 20, 30, (40,50), 60]
    c = 0
    for i in list_data:
        if(isinstance(i,tuple)):
            break
        c += 1
    print(c)
    
main()