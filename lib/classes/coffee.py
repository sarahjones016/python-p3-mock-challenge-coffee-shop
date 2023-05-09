class Coffee:
    def __init__(self, name):
        self.name = name

        self.order_list = []
        self.customer_list = []
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("name must be a string and must have not been previously set")

    name = property(get_name, set_name)
        
    def orders(self, new_order=None):
        from classes.order import Order
        if type(new_order) == Order:
            self.order_list.append(new_order)

        return self.order_list
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer not in self.customer_list and type(new_customer) == Customer:
            self.customer_list.append(new_customer)

        return self.customer_list
    
    def num_orders(self):
        return len(self.order_list)
    
    def average_price(self):
        return sum(self.order_list.price) / len(self.order_list)