#  Write a Python program to sort a tuple by its float element.
#  Sample data:
#  [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#  Expected Output:
#  [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]


def main():
    data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    # for i in data:
    #     print(i[0])
    
    data.sort(key=lambda x: float(x[-1]),reverse=True)

    print(data)



main()