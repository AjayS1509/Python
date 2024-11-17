#  Write a program that asks the user how many days are in a particular month, and
#  what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then
# printsacalendarforthatmonth.Forexample,hereistheoutput fora30-daymonththat
#  beginsonday4(Thursday):

#  SMTWTFS
#      123
#  45678910
#  11121314151617
#  18192021222324
#  252627282930

def main():

    l = ['S','M','T','W','T','F','S']
    days = ''
    for i in l:
        days += i
        days += '  '
    #print(len(days))
    print(days)
    n = 1

    c = 0
    # print(len(l))
        
    for i in range(5):
        s = ""
        for j in range(0,len(l)):
            if(n < 31):
                if(n == 1 and j == 4):
                    s += str(n)
                    s += "  "
                    n += 1
                    c += 1
                elif(c == 0):
                    if(n < 10):
                        s += " "
                    s += "  "
                else:
            
                    s += str(n)
                    s += " "
                    if(n < 10):
                        s += " "
                    n += 1

        print(s)

main()