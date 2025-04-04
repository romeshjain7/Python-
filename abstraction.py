# from abc import ABC, abstractmethod

# # Abstract class
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         self.a="hello"  # Abstract method, no implementation
#         self.b=10

#     @abstractmethod
#     def stop(self):
#         self.c="Pyspiders"
#         self.d=20

# # Concrete class
# class Car(Vehicle):
#     def start(self):
#         print("Car is starting with key ignition.")

#     def stop(self):
#         print("Car is stopping by applying brakes.")

# class Bike(Vehicle):
#     def start(self):
#         print("Bike is starting with self-start.")

#     def stop(self):
#         print("Bike is stopping by pressing brake lever.")

# # Creating objects
# # obj=Vehicle()
# # # obj.start()
# # obj.stop()

# # car = Car()
# # car.start()
# # car.stop()

# # bike = Bike()
# # bike.start()
# # bike.stop()


from abc import ABC, abstractmethod

# Define an abstract class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass  # This is an abstract method, no implementation here.

# Concrete subclass of Animal
class Dog(Animal):
    
    def sound(self):
        a="Bark"
        print(a) # Providing the implementation of the abstract method
        return a

# Create an instance of Dog
dog = Dog()
print(dog.sound())  # Output: Bark

