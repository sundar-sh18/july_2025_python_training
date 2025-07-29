# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"name: {self.name}, age: {self.name}"

# x = Person("sundar",21)
# print(x)


# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a//b
#     def action(self,action,a,b):
#         if(action == 'add'):
#            return self.add(a,b)
#         elif(action == 'mul'):
#            return self.mul(a,b)
#         elif(action == 'div'):
#            return self.div(a,b)
#         elif(action == 'sub'):
#            return self.sub(a,b)

# cal = Calculator()
# act = input("Enter the action : ")
# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
    
# print(cal.action(act,num1,num2))


#INHERITENCE


# class Animal:
#     def Dog(self):
#         print("Dog Barks")

# class Cat(Animal):
#     def cat(self):
#         print("Cat meows")

# animal = Cat()
# animal.Dog()
# animal.cat()



#DATA ENCAPSULATION

# class Person:

#     def setName(self, name):
#         self.name = name

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

#     def getName(self):
#         return self.name

# person = Person()
# person.setName("sundar")
# print(person.getName())
# print(person)


#ABSTRACT METHOD

# from abc import ABC, abstractmethod

# class Shape:
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14*self.radius*self.radius
    
# circle = Circle(5)
# print(f"area of circle: {circle.area()}")