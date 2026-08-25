class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


dog1 = Dog()
cat1 = Cat()

make_sound(dog1)
make_sound(cat1)