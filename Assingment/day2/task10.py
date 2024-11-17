#  grp1 = {"blr" : 5, "chn": 5, "hyd": 5 , "del" : 5 }
#  grp2 = {"blr" : 1, "mum": 2, "noida": 3, "del" : 4 }
#  Expected:
# ==========
#  print(res)
#  {"blr" : 6,
#  "chn" : 5,
#  "hyd" : 5,
#  "del" : 9,
#  "mum" : 2,
#  "noida": 3}

def main():
    grp1 = {"blr" : 5, "chn": 5, "hyd": 5 , "del" : 5 }
    grp2 = {"blr" : 1, "mum": 2, "noida": 3, "del" : 4 }
    res = {}

    for key, value in grp1.items():
        res[key] = value

    for key,value in grp2.items():
        if(key in res):
            res[key] += value
        else:
            #new created
            res[key] = value
    print(res)

    #another method
    res2 = grp1.copy()  # Start with grp1
    for key, value in grp2.items():
        res2[key] = res2.get(key, 0) + value 

main()