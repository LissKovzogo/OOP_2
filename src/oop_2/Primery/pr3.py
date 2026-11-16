class Ship:
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity
        self.cargo =0
    def sail(self):
        print("{} has sailed!".format(self.name))
    def convert_cargo(self):
        cargo_kg = self.cargo*1000
        return cargo_kg
    def name_captain(self,cap):
        self.captain = cap
        print("{} is the captain of the {}!".format(self.captain,self.name))
    def load_cargo(self, weight):
        if self.cargo+weight < self.capacity:
            self.cargo += weight
            print("Loaded {} tons!".format(weight))
        else:
            print("Cannot load that much")
    def unload_cargo(self,weight):
        if self.cargo-weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons!".format(weight))
        else:
            print("Cannot unload that much")
    def free_space(self):
        return self.cargo - self.cargo


def sail_func(name):
    print("{} has sailed!".format(name))

black_pearl = Ship("Black Pearl",800)
black_pearl.sail()

sail_func(black_pearl.name)

print(black_pearl.convert_cargo())

black_pearl.name_captain("Jask Sparrow")
print(black_pearl.name_captain)


black_pearl.load_cargo(600)
black_pearl.unload_cargo(400)
black_pearl.load_cargo(700)
black_pearl.unload_cargo(300)