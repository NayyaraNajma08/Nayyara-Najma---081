class User:
    """Profil pengguna sederhana."""
 
    def __init__(self, first_name, last_name, age, email, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.occupation = occupation
 
    def describe_user(self):
        print(f"User profile for {self.first_name} {self.last_name}:")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")
        print(f"  Occupation: {self.occupation}")
 
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
 
 
users = [
    User("Rani", "Humaira", 36, "rani@example.com", "Surakarta", "Data Analyst"),
    User("Raja", "Bima", 29, "raja@example.com", "Pontianak", "Aerospace Engineer"),
    User("Tsaqiv", "Aqiv", 20, "tsaqiv@example.com", "Sukoharjo", "Teacher"),
]
 
for user in users:
    user.describe_user()
    user.greet_user()
    print()