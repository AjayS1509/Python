#  using for loop
#  print the following outputs
#  output1:----------
#  1
#  2 2
#  3 33
#  4 444
#  5 5555
#  output2:--------
# A
#  B B
#  CCC
#  DDDD

def main():
    n = 5
    for i in range(1,n+1):
        print(" ".join([str(i) for j in range(0,i)]))

    print("\n")
    #-------------------------------------------------------------------
    #with alphabets
    m = 4
    #print(chr(65))
    for i in range(m):
        print(" ".join([str(chr(65+i)) for j in range(0,i+1)]))
main()