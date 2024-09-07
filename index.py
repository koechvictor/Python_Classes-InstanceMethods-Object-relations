class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        
class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name after the coffee is instantiated.")
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Name must be a string with at least 3 characters.")
        
class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("price must be a float between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if hasattr(self, '_price'):
            raise AttributeError("Cannot change the price after the order is instantiated.")
        if not isinstance(value, float) or not (1.0 <= value <= 10.0):
            raise ValueError("price must be a float between 1.0 and 10.0")
        self._price = value
