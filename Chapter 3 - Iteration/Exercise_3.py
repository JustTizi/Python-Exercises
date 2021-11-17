own_age = int(input("How old are you: "))
father_age = int(input("How old is you father: "))
count = 0

if father_age - own_age > own_age:
    while father_age / own_age != 2:

        own_age += 1
        father_age += 1
        count += 1
    print("Within", count, "years your father will have twice your age \nYour father will be", father_age, "and you will be", own_age)
else:
    print("The situation is no longer possible for your ages")