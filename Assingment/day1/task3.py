#  data = "15-aug-1947 10:30:45"
#  using split method split the above data
#  display the following data
#  Expected:------------
#  date is = 15-aug-1947
#  day = 15
#  month = aug
#  year = 1947
#  time is = 10:30:45
#  hours = 10
#  mins = 30
#  secs = 45

def main():
   data = "15-aug-1947 10:30:45"
   date,time = data.split(" ")
   day,month,year = map(str,date.split("-"))
   hour,mins,secs = map(str, time.split(":"))
   print("day = ",day)
   print("month = ",month)
   print("year = ",year)
   print("hours = ",hour)
   print("mins = ",mins)
   print("secs = ",secs)

main()