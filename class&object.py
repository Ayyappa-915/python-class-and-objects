class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("Reataurant Name:{0} and cuisine type:{1}".format(self.restaurant_name,self.cuisine_type))
    def open_restaurant(self):
        print("our Restaurant {0} is open".format(self.restaurant_name))
r=Restaurant("ABHI RUCHI","veg and non-veg")
x=Restaurant("DAWAT","non-veg")
z=Restaurant("LODGE","ac and non-ac")
r.describe_restaurant()
x.describe_restaurant()
z.describe_restaurant()