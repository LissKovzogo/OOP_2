class Pet:
    kind = 'mammal'
    n_pets = 0
    pet_names = []

    def __init__(self,spec,name):
        self.name = name
        self.spec= spec
        self.leg = 4

tom = Pet("cat","Tom")
avacado = Pet('dog','Avacado')
ben = Pet('goldfish','Ben')

Pet.n_pets+=3
print(Pet.n_pets)
print(tom.n_pets)
print(avacado.n_pets)
print(ben.n_pets)

ben.kind = 'fish'
print(Pet.kind)
print(tom.kind)
print(avacado.kind)
print(ben.kind)

tom.pet_names.append(tom.name)
avacado.pet_names.append(avacado.name)
ben.pet_names.append(ben.name)
print(tom.pet_names)

tom.pet_names.append("Tom")
avacado.pet_names.append("Avacado")
ben.pet_names.append("Ben")
print(tom.pet_names)
print(avacado.pet_names)
print(ben.pet_names)

ben.leg =0

Pet.all_specs = [tom.spec,avacado.spec,ben.spec]
avacado.bred = 'corgi'