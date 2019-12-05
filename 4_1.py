pizzas = ["peperonni", "calsone", "4 cheses"]
for pizza in pizzas:
	print(f"I like {pizza} pizza!")
print("I really love pizza!")

animals = ["bear", "dog", "cat", "lion"]
for animal in animals:
	print(f"A {animal} would make a great pet!")
print("Any of these animals would make a great pet!")

friend_pizzas = pizzas[:]

pizzas.append("chiken BBQ")
friend_pizzas.append("veget")

print("My favorite pizzas are: ")
for pizza in pizzas:
	print(pizza)
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
	print(pizza)

print([animal for animal in animals])	