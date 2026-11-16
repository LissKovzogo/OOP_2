class MyClass:
    def __init__(self,arg):
        self.arg = arg

    def do_smt(self):
        print('do something')

my_object = MyClass(10)
my_object.do_smt()
MyClass.do_smt(my_object)