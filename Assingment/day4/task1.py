import sqlite3
import csv

def main():
     f1 = open(r"D:\python\Assingment\day4\data.csv", "w")
     f1.write("name,loc,salary\n")
     f1.write("arun,blr,25000\n")
     f1.write("hari,chn,45000\n")
     f1.write("john,mum,30000\n")
     f1.write("manu,hyd,35000")
     f1.close()

     conn = sqlite3.connect('employees.db')
     cursor = conn.cursor()

     cursor.execute('''
        create table if not exists employees(
                    name text,
                    loc text,
                    salary real
                    );
                    ''')
     
     with open('data.csv','r') as file:
          reader = csv.reader(file)
          next(reader)
          for row in reader:
               cursor.execute('insert into employees (name,loc,salary) values (?,?,?)',row)

     conn.commit()
     conn.close()

     print('data has been stored successfully!')

main()
