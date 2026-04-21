#1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

#создание экземпляра
newRestaurant = Restaurant("Mario's", "Italian")

#вывод
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

#вызов
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
#2
r1 = Restaurant("Mario's", "Italian")
r2 = Restaurant("Sushi Bar", "Japanese")
r3 = Restaurant("Burger King", "Fast Food")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()
