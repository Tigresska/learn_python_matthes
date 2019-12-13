def print_sandwich(*ingridients):
    print("You ordered a sandwich with:")
    for ingridient in ingridients:
        print(f"- {ingridient}")

print_sandwich("mashrooms", "chese", "bacon")
print_sandwich("mashrooms", "chese", "bacon", "tomatos")
print_sandwich("onion", "chese", "bacon")