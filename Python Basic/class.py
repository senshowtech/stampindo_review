class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


# tampung data class
myobjectx = MyClass()
# akses variabel di dalam class
print(myobjectx.variable)
# akses function dalam class
myobjectx.function()


class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name, self.color, self.kind, self.value)
        return desc_str


# panggil class Vehicle
car1 = Vehicle()
# initialisasi data car1 name,color,kind dan value
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

# panggil class Vehicle
car2 = Vehicle()
# initialisasi data car1 name,color,kind dan value
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())