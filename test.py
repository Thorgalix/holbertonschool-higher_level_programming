#!/usr/bin/python3
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_information(self):
        print(f"Car : {self.brand} {self.model}")
        
# Objects création
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Method usage
car1.display_information()
car2.display_information()


