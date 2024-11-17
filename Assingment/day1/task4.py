#  data = "ravi-sales-20,10,40,30"
#  Expected:----------
# total sales = 100
#  min = 10
#  max = 40
#  avg = 20.00

def main():
    data = "ravi-sales-20,10,40,30"
    #sales = data.split("-", 2)[-1].split(",")
    sales = [int(i) for i in data.split("-", 2)[-1].split(",")]

    print("total sales = ",sum(sales))
    print("min = ",min(sales))
    print("max = ",max(sales))
    print("avg = ",(sum(sales)/len(sales)))
main()