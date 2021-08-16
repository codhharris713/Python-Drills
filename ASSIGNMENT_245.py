#main class
class vehicle:
    #attributes of main class
    color = "red"
    style = "truck"
    lot = "123xyz"
    #function for main class
    def typ(self):
        entry_color = input("Color type here: ")
        entry_style = input("Sytle type here: ")
        entry_lot = input("Lot locate here: ")
        if(entry_style == self.style and entry_lot == self.lot):
            print("This vehicle is a {} in lot {}.".format(entry_style, entry_lot))
        else:
            print("Vehicle not found")
#sub class 1
class truck(vehicle):
    color = "blue"
    model = "tacoma"
    part_number = "789abc"
    #function is the same as main class but model and part number
    def typ(self):
        entry_color = input("Color type here: ")
        entry_model = input("Model type here: ")
        entry_part = input("Part Number here: ")
        if(entry_model == self.model and entry_part == self.part_number):
            print("This vehicle is a {} with part number {}.".format(entry_model, entry_part))
        else:
                print("Vehicle and part not found")
#sub class 2
class car(vehicle):
    color = "white"
    model = "leaf"
    part_number = "567asd"
    #function is the same as main class but model and part number 
    def typ(self):
        entry_color = input("Color type here: ")
        entry_model = input("Model type here: ")
        entry_part = input("Part Number here: ")
        if(entry_model == self.model and entry_part == self.part_number):
            print("This vehicle is a {} with part number {}.".format(entry_model, entry_part))
        else:
                print("Vehicle and part not found")
                
#invoke the methods for all classes 
x = vehicle()
x.typ()

y = truck()
y.typ()

z = car()
z.typ()
