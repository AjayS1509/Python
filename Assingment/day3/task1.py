#  Task1:--------
#  depts={
#  101 : "sales",
#  102 : "purch",
#  103 : "accts",
#  104 : "finan"
#  }
#  emps = {
#  "arun" : "blr-101-alpha",
#  "ravi" : "chn-104-beta",
# "hari" : "hyd-102-delta",
#  "manu" : "del-103-omega"
#  }
#  Expected:------------
#  Enter the emp name : ravi
#  location
#  dept id
#  : blr
#  : 104
#  dept name : finan
#  proj name : beta
#  Enter the emp name : john
#  Error- Invalid emp name

def findEmpDetails(name,emps,depts):
        details = []
        for key,value in emps.items():
            if(name == key):
                details = [ele for ele in value.split("-")]
        if(len(details) != 0):
            for key,value in depts.items():
                if(int(details[1]) == key):
                    details.insert(2,value)
        return details

def main():
    depts={
    101 : "sales",
    102 : "purch",
    103 : "accts",
    104 : "finan"
    }
    emps = {
    "arun" : "blr-101-alpha",
    "ravi" : "chn-104-beta",
    "hari" : "hyd-102-delta",
    "manu" : "del-103-omega"
    }

    empName = input("Enter the employee name: ")
    data = findEmpDetails(empName,emps,depts)
    if(len(data) != 0):
        print("location :",data[0],"\ndeptid :",data[1],"\ndept name :",data[2],"\nproj name :",data[3])
    else:
        print("Invalid emp name")

main()

    