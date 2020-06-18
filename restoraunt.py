class Restoraunt:
    def __init__ (self, restaraunt_name, cuisine_type):
        """Initialize restaraunt_name and cuisine_type attributes."""
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Prints information about restaraunt name and cuisine type."""
        print(f"Restaraunt name is {self.restaraunt_name}.")
        print(f"Restaraunt cuisine type is {self.cuisine_type}.")

    def open_restaraunt(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"Reataraunt {self.restaraunt_name} is open.")

    def set_number_served(self, number):
        """Set the number of customers that have been served"""
        self.number_served = number

    def increment_number_served(self, number):
        """Increment the number of customers who’ve been served"""
        self.number_served += number

new_restaraunt = Restoraunt('Rivera', 'Italian')
print(f"{new_restaraunt.restaraunt_name} {new_restaraunt.cuisine_type}")
new_restaraunt.describe_restaurant()
new_restaraunt.open_restaraunt()

new_restaraunt.number_served = 5
print(f"Restaraunt number of served is {new_restaraunt.number_served}.")
new_restaraunt.set_number_served(20)
print(f"Restaraunt number of served is {new_restaraunt.number_served}.")
new_restaraunt.increment_number_served(20)
print(f"Restaraunt number of served is {new_restaraunt.number_served}.")