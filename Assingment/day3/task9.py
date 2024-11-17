#  Given a dictionary of students and their favourite colours:
#  people={'Arham':'Blue','Lisa':'Yellow', 'Vinod:'Purple','Jenny':'Pink'}
#  1. Find out how many students are in the list
#  2. Change Lisa’s favourite colour to "Purple"
#  3. Remove 'Jenny' and her favourite colour
#  4. Sort and print students and their favourite colours alphabetically by name


def main():
    people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
    print(len(people))
    people['Lisa'] = "Purple"
    print(people['Lisa'])
    people.pop('Jenny')
    print(sorted(people.items()))
    

main()