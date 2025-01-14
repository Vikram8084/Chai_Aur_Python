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

# inheritence

class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size


    def fuel_type(self):
        return "Electric Charge"
       

my_tesla = ElectricCar("Tesla", "Model S","85kWh")      
# print(my_tesla.model) 
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())

print(Car.total_car)


my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)
