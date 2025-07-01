#OOP concepts: Encapsulation, Abstraction, Inheritance and Polymorphism
#Encapsulation involves restricting access to data using access modifiers
class Person:
    def __init__(self,name:str,ID:int,age:int):
        self.name = name #public attribute
        self.__ID = ID   #private attribute
        self._age = age  #protected attribute

    def getid(self):
        return self.__ID
    def getage(self):
        return self._age

    def showdetails(self):
        print(f"Name: {self.name} \nID: {self.getid()} \nAge: {self.getage()}")


newperson = Person("Mogambi",580576984,19)
newperson.showdetails()

#Abstraction involves hiding complex implementation details and exposing only those that need to be seen

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def makesound(self):
        pass                   #No implementation details

class Dog(Animal):
    def makesound(self):
        print("Woof!")
germanShepherd = Dog()
germanShepherd.makesound()

#Inheritance involves a class borrowing attributes from a super class(already existing)
#Polymorphism involves a subclass modifying an inherited method

class Student(Person):
    def __init__(self,name,ID,age,studentID):
        super().__init__(name,ID,age)#calls the parent constructor
        self.studentID = studentID

    def showdetails(self):   #Polymorphism
        super().showdetails() #calls the parent version of showdetails
        print(f"StudentID:{self.studentID}")




student1 = Student("Mogambi",580576984, 19)
student1.showdetails()

