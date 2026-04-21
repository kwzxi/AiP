#3
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Rating updated to {self.rating}")

#4
class Cleaner:
    def clean(self):
        print("Уборка выполнена!")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
        self.cleaner = Cleaner()  #+уборщик

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def update_rating(self, new_rating):
        self.rating = new_rating

    def make_clean(self):
        self.cleaner.clean()
