guests = ['Tanya', 'Nikita', 'Nastya', 'Gasya']
for guest in guests:
	print("My friend  " + guest + ", I invite you to launch today!")

exclude = "Nikita"
print("Не сможет прийти " + exclude)
guests.remove(exclude)
for guest in guests:
	print("My friend  " + guest + ", I invite you to launch today!")

print("Great news, more guests will come!")
guests.insert(0, "Danya")
guests.insert(3, "Katya")
guests.append("David")

for guest in guests:
	print("My friend  " + guest + ", I invite you to launch today!")

print("The dining table will not be brought, only two places left!")

for i in range(len(guests)-2):
	del_guest = guests.pop()
	print(del_guest+ ", I'm sorry I had to cancel the invitations.")
for guest in guests:
	print("Dear " + guest + ", the invitation is still valid.")
del guests[0]
del guests[0]

print(guests)
