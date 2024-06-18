# Task 1: Class Creation
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Task 2: Create Method
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Task 3: Inheritance
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name}: {self.sound}"

class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

# Task 4: Polymorphism
class Bird:
    def fly(self):
        return None

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"

# Task 5: Encapsulation
class Encapsulation:
    def __init__(self, public, _private, __protected):
        self.public = public
        self._private = _private
        self.__protected = __protected

# Task 6: Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# Task 7: AverageCalculator
class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)

# Example usage:
# Task 1
student = Student(name="Ivan", age=30, grade="2")
print(student.name, student.age, student.grade)

# Task 2
print(student.display_info())

# Task 3
animal = Animal(name="Lala", sound="")
dog = Dog(name="Lala", sound="Auuuuuuuuuu", breed="spitz")
print(animal.make_sound())
print(dog.make_sound(), dog.breed)

# Task 4
bird = Bird()
sparrow = Sparrow()
penguin = Penguin()
print(bird.fly())
print(sparrow.fly())
print(penguin.fly())

# Task 5
obj = Encapsulation(1, 2, 3)
print(obj.public)
print(obj._private)
print(obj._Encapsulation__protected)  # Note: accessing __protected through name mangling
# print(obj.__protected)  # This line will raise AttributeError

# Task 6
rectangle = Rectangle(width=5, height=4)
print(rectangle.calculate_perimeter())

# Task 7
numbers = [5, 10, 15, 20]
avg_calculator = AverageCalculator(numbers)
print(avg_calculator.calculate_average())
