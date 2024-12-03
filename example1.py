class Dog:
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
    def display_dog(self):
        print("Breed of the dog is:",self.breed)
        print("Name of the dog is:",self.name)
        print("Age of the '{0}' dog is:".format(self.name),self.age)
d1=Dog("chinni","siberian Husky","3 years")
print()
d1.display_dog()
