class Vehicle:

    wheels = 4

    def __init__(self, brand):
        self.brand = brand


vehicle1 = Vehicle("Toyota")
vehicle2 = Vehicle("Honda")

print(vehicle1.brand, vehicle1.wheels)
print(vehicle2.brand, vehicle2.wheels)