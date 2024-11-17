# Task4:
# =======
#  Define a function overlapping () that takes two lists and returns True
#  if they have at least one member in common, False otherwise.

def overlapping(list1,list2):
    for ele in list1:
        if(ele in list2):
            return True 
        return False

list1=[1,2,3,4]
list2=[5,6,7,8]

res = overlapping(list1,list2)
print(res)

