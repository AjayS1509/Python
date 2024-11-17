# Task10:-
# ========

# write a program to convert the file contents of upper case 

# Enter the file name : one.txt

# Enter the output file : out.txt

# contents of one.txt:-
# ---------------------
# hello world of unix was
# the output of the above
# program which was given


# contents of out.txt:-
# ---------------------
# HELLO WORLD OF UNIX WAS
# THE OUTPUT OF THE ABOVE
# PROGRAM WHICH WAS GIVEN
def convert_uppercase(val):
    final_val = ''
    for ele in val:
        if(ele.isalpha()):
            final_val += ele.upper()
        else:
            final_val += ele
    return final_val


def main():
    f1 = open('one.txt','r')
    #res = [lines.strip() for lines in f1.readlines()]
    res = f1.readlines()
    print(res)

    l = []
    for value in res:
        l.append(convert_uppercase(value))

    print(l)

    # write data into file
    with open("out.txt",'w') as outfile:
        outfile.write("".join(l))
        print("data written in file successfully!")


main()