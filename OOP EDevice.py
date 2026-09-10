class ElectronicDevice:

    def __init__(self, name, brand, price):
        self.__name = name
        self.__brand = brand
        self.__price = price

    def GetName(self):
        return self.__name

    def GetBrand(self):
        return self.__brand

    def GetPrice(self):
        return self.__price

    def calculate_discounted_price(self):
        price = self.__price

        if price > 500:
            price = price * 0.85
        elif price >= 300:
            price = price * 0.90

        return price

    def display_device_info(self):
        print("Device Name:", self.__name)
        print("Brand:", self.__brand)
        print("Price: $" + str(self.__price))


class SmartPhone(ElectronicDevice):

    def __init__(self, name, brand, price, operating_system):
        super().__init__(name, brand, price)
        self.__operating_system = operating_system

    def GetOS(self):
        return self.__operating_system

    def calculate_total_cost(self, quantity):
        total_cost = self.GetPrice() * quantity

        if quantity >= 3:
            total_cost = total_cost * 0.90

        if quantity >= 5:
            total_cost = total_cost * 0.95

        if quantity >= 10:
            total_cost = total_cost - 50

        return total_cost

    def calculate_discounted_price(self):
        price = self.GetPrice()

        if self.__operating_system == "iOS":
            price = price * 0.80
        elif self.__operating_system == "Android":
            price = price * 0.85
        else:
            price = price * 0.90

        return price


phone = SmartPhone("iPhone 18", "Apple", 4000, "iOS")

discounted_price = phone.calculate_discounted_price()

print("Discounted price:", discounted_price)
