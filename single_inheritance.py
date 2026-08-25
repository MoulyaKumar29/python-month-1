class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    pass


car1 = Car()

car1.start()