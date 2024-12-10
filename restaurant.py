
class Restaurant:

    def __init__(self, restaurantName, cuisineType):

        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
    
    def describe(self):

        print(f"Welcome to {self.restaurantName}, the best {self.cuisineType} restaurant in town")
    
    def open(self):

        print(f"{self.restaurantName} is open!")

res1 = Restaurant("Maira's", "Chinese")
print(res1.restaurantName)
print(res1.cuisineType)
res1.describe()
res1.open()
