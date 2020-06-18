class User:
    def __init__(self, first_name, last_name, nick_name, age, priveliges):
        """
        Initialize first_name, last_name, nick_name, age, priveliges,
        login_attempts attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.age = age
        self.priveliges = priveliges
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user’s information."""
        print(f"\nUser information: ")
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"nick_name: {self.nick_name}")
        print(f"age: {self.age}")
        print(f"priveliges: {self.priveliges}")
        print(f"login attempts: {self.login_attempts}")

    def great_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.nick_name}!")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0


user1 = User('Anastasiia', 'Okataia', 'Tigresska', 29, 'admin')
user1.describe_user()
user1.great_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.describe_user()
user1.reset_login_attempts()
print(user1.login_attempts)