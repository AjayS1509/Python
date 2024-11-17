# sent = "today is monday workday weekday"
#  # using .count method display no of times "day" is repeated
#  # using .index method get the index all the "day"
#  Expected:
# ===========
#  Total no time "day" is repeated is = 4
#  first occurance index = 2
#  second occurance index = 12
#  third occurance index = 20
#  fourth occurace index = 2

def main():
    #using count method
    sent = "today is monday workday weekday"
    print(sent.count("day"))

    #using index method
    sub = "day"
    indices = []
    start = 0

    while start < len(sent):
        index = sent.find(sub, start)
        if index == -1:
            break
        indices.append(index)
        start = index + len(sub)  # Move past the current occurrence

    print(f"first occurance index =  {indices[0]}")
    print(f"second occurance index = {indices[1]}")
    print(f"third occurance index = {indices[2]}")
    print(f"fourth occurace index = {indices[3]}")

main()