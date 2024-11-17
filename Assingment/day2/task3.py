#  sales = ["dvd-50", "prn-30", "mon-10", "hdd-55", "cpu-20"]
#  Problem:----------
#  >>filter out product name if quantity >=40
#  >>Store the resultant in a new list
#  >>filter out product name if quantity <40
#  >>Store the resultant in a new list
#  Expected:------------
#  above40 = ["dvd", "hdd"]
#  below40 = ["prn", "mon", "cpu"]

def main():
    sales = ["dvd-50", "prn-30", "mon-10", "hdd-55", "cpu-20"]
    # above40 = list(map(lambda x:  int(x.split("-")[-1]),sales))
    res1 =  [i.split("-")[0]  for i in sales if(int(i.split("-")[-1]) >= 40)]
    print(res1)
    res2 = [i.split("-")[0]  for i in sales if(int(i.split("-")[-1]) < 40)]
    print(res2)
main()