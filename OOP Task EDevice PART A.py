# Part A(i)
#parent class for electronic devices.

class ElectronicDevice:

    # Name, brand and price are given when the object is created
    def __init__(self, name, brand, price):
        self.__name = name
        self.__brand = brand
        self.__price = price

# Part A(ii)
#values of the private attributes

    def GetName(self):
        return self.__name


    def GetBrand(self):
        return self.__brand


    def GetPrice(self):
        return self.__price

# Part A(iii)
# Calculates the discounted price depending on the original price

    def calculate_discounted_price(self):

        price = self.__price

        if price > 500:
            price = price * 0.85

        elif price >= 300:
            price = price * 0.90

        return price

# Part A(v)
# Displays the information about the electronic device.

    def display_device_info(self):
        print("Device Name:", self.__name)
        print("Brand:", self.__brand)
        print("Price: $" + str(self.__price))

# Part B(i)
# SmartPhone is a child class of ElectronicDevice.

class SmartPhone(ElectronicDevice):

    # Constructor takes the attributes from the parent class and also takes operating_system.
    def __init__(self, name, brand, price, operating_system):
        super().__init__(name, brand, price) # Sends name, brand and price to the parent constructor

        self.__operating_system = operating_system # Stores the operating system as a private attribute

# Part B(ii)
# Calculates the total cost based on the quantity purchased.

def calculate_total_cost(self, quantity):

    # Work out the original total
    total_cost = self.GetPrice() * quantity

    # 10% discount for 3 or more phones
    if quantity >= 3:
        total_cost = total_cost * 0.90

    # Additional 5% discount for 5 or more phones
    if quantity >= 5:
        total_cost = total_cost * 0.95

    # Take $50 off for 10 or more phones
    if quantity >= 10:
        total_cost = total_cost - 50

    return total_cost

# Part C
# This method overrides the calculate_discounted_price()
# method from the parent class.

    def calculate_discounted_price(self):

        price = self.GetPrice()

        if self.__operating_system == "iOS":
            price = price * 0.80

        elif self.__operating_system == "Android":
            price = price * 0.85

        else:
            price = price * 0.90

        return price

# Part D(i)
# Create a SmartPhone object using the values given in the question.

phone = SmartPhone("iPhone 18", "Apple", 4000, "iOS")

# Calculate the discounted price.
discounted_price = phone.calculate_discounted_price()

# Display the result.
print("Discounted price:", discounted_price)
