active = "yes"
while active.lower() == "yes":
    age = int(input("How old are you? "))
    if age >0 and age < 3:
        cena = 0
    elif age >= 3 and age <= 12:
        cena  = 10
    elif age > 12:
        cena = 15
    print(f"The ticket costs {cena}$.") 
    active = input("Would you like to continue? ")
    
    