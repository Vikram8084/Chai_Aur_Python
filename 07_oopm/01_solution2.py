# Create a Car Class with attributes like brands and models .Then create an instance of this class

class Car:
    # brand = None
    # model = None
    total_car = 0


    def __init__(self, brand, model):#init constructor hai self linkage bana raha hai
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():#static method likhne ke baad self nhi likhna hota hai
        return "Cars are means of transport"

# inheritence

class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size


    def fuel_type(self):
        return "Electric Charge"
       

my_tesla = ElectricCar("Tesla", "Model S","85kWh")   

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))
# print(my_tesla.model) 
# print(my_tesla.full_name())
# print(my_tesla.get_brand())

my_car = Car("Tata", "Safari")
Car("Tata","Nexon")

print(my_car.general_description())
# print(Car.general_description())
# print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())

print(Car.total_car)


my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)

class Battery:
    def battery_info(self):
        return "this is battery"


class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
