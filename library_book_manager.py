class Book:

    def show_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


book1 = Book()
book2 = Book()

book1.title = "Python Programming"
book1.author = "John"
book1.price = 450

book2.title = "C Programming"
book2.author = "Robert"
book2.price = 400

print("Book 1")
book1.show_details()

print()

print("Book 2")
book2.show_details()