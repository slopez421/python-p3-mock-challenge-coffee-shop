class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise ValueError("Name cannot be changed.")
        elif isinstance(name, str) and 3 <= len(name):
            self._name = name
        else:
            raise ValueError("Name must be a str equal to 3 characters or greater.")

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        unique_customers = []
        for order in Order.all:
            if order.coffee == self and order.customer not in unique_customers:
                unique_customers.append(order.customer)
        return unique_customers
    
    def num_orders(self):
        count = 0
        for order in Order.all:
            if order.coffee == self:
                count += 1
        return count
    
    def average_price(self):
        all_prices = [order.price for order in Order.all if order.coffee == self]
        return sum(all_prices) / len(all_prices)

class Customer:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("name should be a str between 1 an 15 characters.")
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        unique_coffees = []
        for order in Order.all:
            if order.customer == self and order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError("Customer should be an instance of the Customer class.")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise ValueError("Coffee should be an instance of the Coffee class.")
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, "price"):
            return
        if isinstance(price, float) and float(1.0) <= price <= float(10.0):
            self._price = price
        else:
            raise ValueError("Price should be a number between 1.0 and 10.0")