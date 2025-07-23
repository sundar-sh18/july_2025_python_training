# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"name: {self.name}, age: {self.name}"

# x = Person("sundar",21)
# print(x)


class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a//b
    def action(self,action,a,b):
        if(action == 'add'):
           return self.add(a,b)
        elif(action == 'mul'):
           return self.mul(a,b)
        elif(action == 'div'):
           return self.div(a,b)
        elif(action == 'sub'):
           return self.sub(a,b)
            
        


cal = Calculator()
act = input("Enter the action : ")
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
    
print(cal.action(act,num1,num2))