user_names = ["Tigresska", "Tyushka", "admin", "gasik", "nasik"]
if user_names:
	for user in user_names:
		if user.lower() == "admin":
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Hello {user}, thenk you for logging in again.")
else:
	print("We need to find some users!")


current_users = ["Tigresska", "Tyushka", "admin", "gasik", "nasik"]	
new_users = ["tigresska", "Reawer", "admin", "LOL", "Qwerty"]
for user in new_users:
	if user.lower() in [item.lower() for item in current_users]:
		print(f"User {user} must select a new username.")
	else:
		print(f"Username {user} is availible.")

numbers = [value for value in range(1,10)]
for value in numbers:
	if value == 1:
		print(f"{value}st")	
	elif value == 2:
		print(f"{value}nd")
	elif value == 3:
		print(f"{value}rd")
	else:
		print(f"{value}th")