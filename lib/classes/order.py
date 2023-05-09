
from classes.coffee import Coffee
from classes.customer import Customer

all = []

class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        coffee.orders(self)
        customer.orders(self)

        coffee.customers(self.customer)
        customer.coffees(self.coffee)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if type(price) == int or float and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception("price must be a number and be between 1 and 10")

    price = property(get_price, set_price)

    def get_customer(self):
        return self._customer

    def set_customer(self, customer):
        if type(customer) == Customer:
            self._customer = customer
        else:
            raise Exception("Must be of type Customer")

    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee

    def set_coffee(self, coffee):
        if type(coffee) == Coffee:
            self._coffee = coffee
        else:
            raise Exception("Must be of type Coffee")

    coffee = property(get_coffee, set_coffee)


