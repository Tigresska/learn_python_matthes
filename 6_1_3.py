famous_person1 = {
	'first_name': 'Angelina',
	'last_name': 'Joile',
	'age': '50',
	'city': 'New York',
	}
famous_person2 = {
	'first_name': 'Bred',
	'last_name': 'Pitt',
	'age': '52',
	'city': 'Washington',
	}
famous_person3 = {
	'first_name': 'Lewis',
	'last_name': 'Hamilton',
	'age': '38',
	'city': 'London',
	}		
people = [famous_person1, famous_person2, famous_person3]
for person in people:
	print()
	for key, value in person.items():
		print(f"{key}: {value}")