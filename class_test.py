from abc import ABCMeta, abstractmethod

class Animal(object):
    """
        this is an abstract animal method used
        as a template for all other animal
        classes
    """

    __metaclass__ = ABCMeta
    
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def can_speak(animal):
        return animal.can_speak()

class Dog(Animal):
    def can_speak(self):
        return False

class Person(Animal):
    def can_speak(self):
        return True

class Turtle(Animal):
    color = 'green'
    def can_speak(self):
        return False