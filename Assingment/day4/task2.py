import sqlite3
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
# print(rows)

with open('employees.txt', 'w') as f1:

    f1.write("name,loc,salary\n")
    
    for elem in rows:
        line = ",".join(map(str, elem))
        # print(line)
        f1.write(line + "\n")

conn.close()

print("Data has been stored in employees.txt.")