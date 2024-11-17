#  Modify the program above using a while loop so it prints out all of the factorial
#  values that are less than 2 billion. (You should be able to do this without looking at the
#  output of the previous exercise.)


def fact(n):
    if(n <= 1):
        return n
    else:
        return n * fact(n - 1)

def main():
    n = 1
    while(1):
        print("factorial = ",fact(n))
        n += 1
    

main()