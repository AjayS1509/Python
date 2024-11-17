#  Task1:
# =======
#  Given:
# =======
#  name = "harshavardhan"
#  Expected:
# ==========
#  res1 = "harshavardhaN" # convert the last letter to upper case
#  res2 = "HarshavardhaN" # convert the first & last letter to upper case
#  res3 = "harshavar-DHAN"# Convert the last 4 letters to upper case
#  res4 = "harshavar-NDHD"# Convert the last 4 letters to upper case & reverse it

def main():
    
    name = "harshavardhan" 

    print(name[:-1].lower()+ name[-1].upper())
    print(name[0].upper() + name[1:-1].lower() + name[-1].upper())
    print(name[:-4].lower() + name[-4:].upper())
    print(name[:-4].lower()+ name[-4:][::-1].upper())
main()