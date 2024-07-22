class Flower:

    def __init__(self, name, petals, price):
        self.set_flower_name(name)
        self.set_petals_number(petals)
        self.set_flower_price(price)
    
    def set_flower_name(self, name):
        try:
            self._name = str(name)
        except:
            raise ValueError("Invalid value for name, must be string")

    def get_flower_name(self):
        return self._name
    
    def set_petals_number(self, petals):
        try:
            self._petals = int(petals)
        except:
            raise ValueError("Invalid value for petals, must be number")

    def get_petals_number(self):
        return self._petals
    
    def set_flower_price(self, price):
        try:
            self._price = float(price)
        except:
            raise ValueError("Invalid value for price, must be float")
    
    def get_flower_price(self):
        return self._price
    

flower = Flower("Rose", 6, 5.4)

print(f"Flower name: {flower.get_flower_name()}")
print(f"Number of petals: {flower.get_petals_number()}")
print(f"Price: {flower.get_flower_price()}")

# Ourput
# Flower name: Rose
# Number of petals: 6
# Price: 5.4