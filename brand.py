# class Bicycle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def get_age(self, current_year):
#         return current_year - self.year
#
#
#
# bike = Bicycle("Cube", "AIm Ex 2023", 2023)
# print(f": {bike.get_age(2024)} ")

# class Doctor:
#     def __init__(self, name):
#         self.name = name
#
# class Patient:
#     def __init__(self, name):
#         self.name = name
#
#     def introduce_doctor(self, doctor1):
#         print(f"My doctor is {doctor1.name}")
#
#
# doctor1 = Doctor("Mr.Ivanov")
# patient1 = Patient("Vasya")
# patient1.introduce_doctor(doctor1)


# class Vehicle:
#     def move(self):
#         print("Vehicle moves")
#
# class Car(Vehicle):
#     def move(self):
#         print("Car drives")
#
#
# car = Car()
# car.move()

class Pen:

    def write(self):
        print("Writing")

class Highlighter:
    def highlight(self):
        print("HighLighting")

class Marker(Pen,Highlighter):
    pass

my_marker = Marker()
my_marker.write()
my_marker.highlight()






