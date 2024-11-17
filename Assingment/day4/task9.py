#  Write a program to display the first and last word of a given file
#  Enter a filename : one.txt
#  contents of one.txt:----------------------
#  hello world of unix was
#  the output of the above
#  program which was given
#  Expected output is :----------------------
#  hello- was
#  the- above
#  program- given


def main():
    #read data from file
    f1 = open('one.txt','r')
    res = [line.strip() for line in f1.readlines()]
    #print(res)

    #res2 = ["".join([inner[0]+'- '+inner[-1] for inner in ele.split(" ")]) for ele in res]
    res2 = [i[0]+"- "+i[-1] for i in [ele.split(" ") for ele in res]]
    #print(*res2)
    for i in res2:
        print(i)
    f1.close()

main()