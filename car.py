class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odo = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def readOdo(self):
        
        print(f"This car has {self.odo} miles on it")


# Create an instance of the Car class
my_new_car = Car('audi', 'a4', 2024)

# Print the descriptive name of the car
print(my_new_car.get_descriptive_name())

my_new_car.readOdo()
my_new_car.odo = 2000
my_new_car.readOdo()