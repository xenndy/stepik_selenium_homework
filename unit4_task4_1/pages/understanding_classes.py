#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# # Создаем класс Car
# class Car:
 
#     # создаем атрибуты класса
#     car_count = 0
 
#     # создаем методы класса
#     def start(self, name, make, model):
#         print("Двигатель заведен")
#         self.name = name
#         self.make = make
#         self.model = model
#         Car.car_count += 1

#     @staticmethod
#     def get_class_details():
#         print ("Это класс Car")


# car_a = Car()
# car_b = Car()
# car_c = Car()

# car_a.start("Corrola", "Toyota", 2015)  
# print(car_a.name)  
# print(car_a.car_count)

# car_b.start("5x", "BMW", "2014")
# print(car_b.name, car_b.make)
# print(car_b.car_count)

# car_c.start("Fit", "Honda", 2013)
# print(car_c.name)
# print(car_c.car_count)

# Car.get_class_details()


# class Square:
 
#     @staticmethod
#     def get_squares(a, b):
#         return a*a, b*b
 
# print(Square.get_squares(3, 5))


# class Car:
#     # создание методов класса
#     def __str__(self):
#         return "Car class Object"
 
#     # создание методов класса
#     def start(self):
#         print ("Двигатель заведен")
 
# car_a = Car()  
# print(car_a)
# # print(car_a.start)


# # создаем класс Car
# class Car:
#     message_1 = "Двигатель заведен"
#     def start(self):
#         message_2 = "Двигатель stopped"
#         return message_2


# car_a = Car()
# print(car_a.message_1)
# print(car_a.start())



# class Car:  
#     def __init__(self):
#         print ("Двигатель заведен")
#         self.name = "corolla"
#         self.__make = "toyota"
#         self._model = 1999
    
#     def print_make(self):
#         return self.__make

# car_a = Car()
# # print(car_a.name)
# print(car_a.print_make())



# # Создание класса Vehicle
# class Vehicle:
#     def vehicle_method(self):
#         print("Это родительский метод из класса Vehicle")

# # Создание класса Car, который наследует Vehicle
# class Car(Vehicle):
#     def car_method(self):
#         print("Это метод из дочернего класса")


# car_a = Vehicle()
# car_b = Car()
# car_a.vehicle_method()
# car_b.car_method()
# car_b.vehicle_method()


# # создаем класс Vehicle
# class Vehicle:  
#     def vehicle_method(self):
#         print("Это родительский метод из класса Vehicle")
 
# # создаем класс Car, который наследует Vehicle
# class Car(Vehicle):  
#     def car_method(self):
#         print("Это дочерний метод из класса Car")
 
# # создаем класс Cycle, который наследует Vehicle
# class Cycle(Vehicle):  
#     def cycleMethod(self):
#         print("Это дочерний метод из класса Cycle")


# car_a = Car()  
# car_a.vehicle_method() # вызов метода родительского класса
# car_b = Cycle()  
# car_b.vehicle_method() # вызов метода родительского класса


class Camera:  
    def camera_method(self):
        print("Это родительский метод из класса Camera")
 
class Radio:  
    def radio_method(self):
        print("Это родительский метод из класса Radio")
 
class CellPhone(Camera, Radio):  
     def cell_phone_method(self):
        print("Это дочерний метод из класса CellPhone")


p = CellPhone()

p.radio_method()
p.camera_method()


# # создание класса Vehicle
# class Vehicle:  
#     def print_details(self):
#         print("Это родительский метод из класса Vehicle")
 
# # создание класса, который наследует Vehicle
# class Car(Vehicle):  
#     def print_details(self):
#         print("Это дочерний метод из класса Car")
 
# # создание класса Cycle, который наследует Vehicle
# class Cycle(Vehicle):  
#     def print_details(self):
#         print("Это дочерний метод из класса Cycle")


# car_a = Car()
# car_b = Cycle()

# car_a.print_details()
# car_b.print_details()



# # создаем класс Car
# class Car:

#     # создаем конструктор класса Car
#     def __init__(self, model):
#         # Инициализация свойств.
#         self.model = model

#     # создаем свойство модели.
#     @property
#     def model(self):
#         return self.__model

#     # Сеттер для создания свойств.
#     @model.setter
#     def model(self, model):
#         if model < 2000:
#             self.__model = 2000
#         elif model > 2018:
#             self.__model = 2018
#         else:
#             self.__model = model

#     def getCarModel(self):
#         return "Год выпуска модели " + str(self.model)

# carA = Car(2088)  
# print(carA.getCarModel())













