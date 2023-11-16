from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight: int = 0
    fuel: int = 0
    fuel_consumption: int = 0
    started: bool = False

    def __init__(self, weight: int, fuel: int, fuel_consumption: int):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        fuel_require = self.fuel_consumption * distance
        if self.fuel >= fuel_require:
            self.fuel -= fuel_require
        else:
            raise exceptions.NotEnoughFuel
