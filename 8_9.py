def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(0,len(magicians)):
        new_magican = "Great " + magicians.pop(i)
        magicians.insert(i,new_magican)
    return magicians



magicians = ["Nastya", "Tanya", "Maria"]

show_magicians(magicians)
new_magicans = make_great(magicians[:])
print("Magicians: ")
show_magicians(magicians)
print("New magicians: ")
show_magicians(new_magicans)