# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#     def __init__(self, fuel_quantity, fuel_consumption):
#         self.fuel_quantity = fuel_quantity
#         self.fuel_consumption = fuel_consumption
#
#     @abstractmethod
#     def drive(self, distance):
#         pass
#
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel
#
#
# class Truck(Vehicle):
#     _CONSUMPTION_PER_KM = 1.6
#     def drive(self, distance):
#         consumption = (self.fuel_consumption + self._CONSUMPTION_PER_KM) * distance
#         if self.fuel_quantity >= consumption:
#             self.fuel_quantity -= consumption
#
#     def refuel(self, fuel):
#         self.fuel_quantity += 0.95 * fuel
#
#
# class car(Vehicle):
#     _CONSUMPTION_PER_KM = 0.9
#     def drive(self, distance):
#         consumption = (self.fuel_consumption + self._CONSUMPTION_PER_KM) * distance
#         if self.fuel_quantity >= consumption:
#             self.fuel_quantity -= consumption
#
#
# car = car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance: int):
        fuel_needed = (self.fuel_consumption + self._CONSUMPTION_PER_KM) * distance
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed

    @property
    @abstractmethod
    def _CONSUMPTION_PER_KM(self):
        ...


class Truck(Vehicle):
    _CONSUMPTION_PER_KM = 1.6

    def refuel(self, fuel):
        super().refuel(fuel * 0.95)


class Car(Vehicle):
    _CONSUMPTION_PER_KM = 0.9

    def refuel(self, fuel):
        super().refuel(fuel)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)