
#creating the class vehicle
class vehicle:
#define the attributes of the class
    energy_source = 'gasoline engine'
    physical_form = 'truck'
    number_of_doors = 4
#1st child class
class toyota_tacoma (vehicle): 
    price = 23.269
    mileage = 60.000
#2nd child class
class toyota_tundra (vehicle):
    price = 24.300
    mileage = 50.000
