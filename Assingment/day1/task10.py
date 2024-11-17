# data="10-50-25-12-85"
#  Expected:
# ==========
#  res="11-51-26-13-86"

def main():
    data="10-50-25-12-85"
    n = "-".join([str(j) for j in [int(i)+1 for i in data.split("-")]])
    print(n)

main()
