class Restaurant:
    """Model sederhana sebuah restoran."""
 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
 
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
 
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
 
 
restaurant_1 = Restaurant("Osteria Pizzane", "Italian")
restaurant_2 = Restaurant("Kyoto Ramen", "Japanese")
restaurant_3 = Restaurant("Chefkim", "Korean")
 
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
 