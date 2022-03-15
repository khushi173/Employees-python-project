'''class calc1:
    def addition(self,a,b):
        return a+b
class calc2:
    def multiplication(self,a,b):
        return a*b
class calc3(calc1,calc2):
    def subtraction(self,a,b):
        return a-b
a = calc3()
print(a.subtraction(5,4))
print(a.multiplication(5,4))
print(a.addition(5,4))
print(issubclass(calc3, calc2))
print(isinstance(a, calc2))


class A:
    def mk(self):
        print('i am from class A')

class B:
    def mk(self):
        print('i am from class B')
class C(A,B):
    def __init__(self):
        print('class C is constructed ')
#f =C()
#method resolution order
#f.mk()
#print(C.mro())

#mthod overriding
class D(A):
    def mk(self):
        print('i am from class D')
#g=D()
#g.mk()

#method overloading and operator over;oading

 #data abstraction
class Student:
    __count = 0
    def __init__(self):
        Student.__count +=1
    def printCount(self):
        print('count is:', Student.__count)

stud1 = Student()
stud1.printCount()
#print(stud1._Student__count)
#print(stud1.__count)

#super()

class Animal(object):
    def __init__(self, animal_type):
        print('Animal Type', animal_type)
class Mammal(Animal):
    def __init__(self):

            #superclass
        super().__init__('Mammal')
        print('Mammal gives birth directly')
dog = Mammal()



class Animal(object):
    def __init__(self, PetName):
        print(PetName, 'is a warm-blooded animal.')


class Dog(Animal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()'''



