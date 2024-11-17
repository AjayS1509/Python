#  Defineaprocedurehistogram()that takesalistof integersandprintsahistogram
#  tothescreen.Forexample,histogram([4,9,7])shouldprint thefollowing
#  ****
#  *********
#  *******

def histogram(data):
    for i in data:
        print("".join([str('*') for k in range(i)]))

def main():
    data = [4,9,7]
    histogram(data)
    
main()
