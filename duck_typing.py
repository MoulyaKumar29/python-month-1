class Car:

    def start(self):
        print("Car started")


class Bike:

    def start(self):
        print("Bike started")


def start_vehicle(vehicle):
    vehicle.start()


car1 = Car()
bike1 = Bike()

start_vehicle(car1)
start_vehicle(bike1)