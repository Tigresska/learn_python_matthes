sandwich_orders = ["Bacon", "pastrami", "Bagel toast", "pastrami", "Barros Jarpa", "Chicken", "pastrami"]
finish_sandwiches = []
print("Pastrami are no more.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich")
    finish_sandwiches.append(current_sandwich)
print(f"Finish sanwiches: {finish_sandwiches}")