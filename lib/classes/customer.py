class Customer:
    def __init__(self, name):
        self.name = name

        self.order_list = []
        self.coffee_list = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("name must be a string and be between 1 and 15 characters long")

    name = property(get_name, set_name)
        
    def orders(self, new_order=None):
        from classes.order import Order
        if type(new_order) == Order:
            self.order_list.append(new_order)
            
        return self.order_list
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee not in self.coffee_list and type(new_coffee) == Coffee:
            self.coffee_list.append(new_coffee)

        return self.coffee_list
    
    def create_order(self, coffee, price):
        pass