class Payment:

    def pay(self, amount):
        print("Processing payment of ₹", amount)


class UPI(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class Card(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Card")


class Cash(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Cash")


def process_payment(payment_method, amount):
    payment_method.pay(amount)


upi = UPI()
card = Card()
cash = Cash()

process_payment(upi, 500)
process_payment(card, 1000)
process_payment(cash, 300)