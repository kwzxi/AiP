class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, location, hours, flavors=["Vanilla", "Chocolate"]):
        super().__init__(restaurant_name, "Ice Cream")
        self.flavors = flavors
        self.location = location
        self.hours = hours  #время работы

    def show_flavors(self):
        print("Доступные сорта:", ", ".join(self.flavors))

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Добавлен сорт: {flavor}")
        else:
            print(f"Сорт {flavor} уже есть")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Удален сорт: {flavor}")
        else:
            print(f"Сорт {flavor} не найден")

    def has_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт {flavor} есть в наличии")
            return True
        else:
            print(f"Сорт {flavor} отсутствует")
            return False

    def serve_stick_icecream(self):
        print("Подаем мороженое на палочке!")

    def serve_soft_icecream(self):
        print("Подаем мягкое мороженое!")

