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

    # this function is called every time a new order is created    
    # including "if new_order" ensures that "None" doesn't get added to the list when a new order isn't provided
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and type(new_order) == Order:
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
        # return sum(self.order_list.price) / len(self.order_list)
        return sum([order.price for order in self.order_list]) / len(self.order_list)
    
        # total = 0
        # for order in self.order_list:
        #     total += order.price
        
        # return total / len(self.order_list)