class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def show_info(self):
        return f"Vehicle Name: {self.name}, Speed: {self.speed} km/h"


class Car(Vehicle):
    def __init__(self, name, speed, doors):
        super().__init__(name, speed)
        self.doors = doors

    def show_info(self):
        return f"Car Name: {self.name}, Speed: {self.speed} km/h, Doors: {self.doors}"


class Bike(Vehicle):
    def __init__(self, name, speed, type_of_bike):
        super().__init__(name, speed)
        self.type_of_bike = type_of_bike

    def show_info(self):
        return f"Bike Name: {self.name}, Speed: {self.speed} km/h, Type: {self.type_of_bike}"


# Example usage
vehicle = Vehicle("Generic Vehicle", 80)
car = Car("Sedan", 120, 4)
bike = Bike("Mountain Bike", 30, "Off-road")

print(vehicle.show_info())  # Output: Vehicle Name: Generic Vehicle, Speed: 80 km/h
print(car.show_info())      # Output: Car Name: Sedan, Speed: 120 km/h, Doors: 4
print(bike.show_info())     # Output: Bike Name: Mountain Bike, Speed: 30 km/h, Type: Off-road
