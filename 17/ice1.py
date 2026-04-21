class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name, "Ice Cream")
        self.flavors = ["Vanilla", "Chocolate", "Strawberry"]

    def show_flavors(self):
        print("Доступные сорта мороженого:", ", ".join(self.flavors))

#создание экземпляра и вызов метода
stand = IceCreamStand("Мороженое ням")
stand.show_flavors()