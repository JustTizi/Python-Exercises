for i in range(1, 5):
    print("Information for member", i)
    name = input("Name: ")
    age = int(input("Age: "))
    years_as_member = int(input("Member for how many years: "))
    if age < 12:
        member_fee = 20
        if years_as_member >= 5:
            member_fee *= 0.9
        print("Member fee for", name, "=", member_fee, end="\n\n")
    elif 12 <= age <= 18:
        member_fee = 50
        if years_as_member >= 5:
            member_fee *= 0.9
        print("Member fee for", name, "=", member_fee, end="\n\n")
    else:
        member_fee = 95
        if years_as_member >= 5:
            member_fee *= 0.9
        print("Member fee for", name, "=", member_fee, end="\n\n")