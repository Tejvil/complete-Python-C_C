

class Dog:   # creating a own blueprint of type Dog .
    
    def __init__(self, name, age):   # instanciate the object as soon as it is created. 
        self.name = name        # created an attribute of class Dog
        self.age = age
        
    def bark(self):  # created a method (function inside of a class).
        print("bark")
        
    def get_name(self):
        return self.name
        
    def get_age(self):
        return self.age
        
# d= Dog()    # Dog() is a instance of class Dog. here we have created a new instance of a class Dog. 
# d is an object of type Dog.   print (type(d))
