class Human:
    def __init__(self, name = None, age = None):
        self.name = name 
        self.age = age   

 
    def say_hello(self):
        if type(self.name) is str:
            print(self.name)
        else:
            print('Name ne str')
        if type(self.age) is int:
            print(self.age)
        else:
            print('Age ne int')
        return(print('my name is', self.name))
var = Human(name = 'Valli' , age = 23)  
print(var.say_hello())
pass 

class Builder(Human):
    def __init__(self, name = None, age = None, position = None):
        self.position = position
        self.name = name 
        self.age = age
    def say_hello(self):
        if type(self.name) is str:
            print(self.name)
        else:
            print('Name ne str')
        if type(self.age) is int:
            print(self.age)
        else:
            print('Age ne int')
        return(print('my name is', self.name, self.position))
bil = Builder(name = 'Vasya' , age = 23, position = 'Bilder' )  
print(bil.say_hello())
 
class Writer(Human):
    def my_bookc(*book):
        boks = 0
        for element in book:
            if str(type(element)) not in book :
                boks += 1
            else:
                print('ne stroka')
        print('I write', boks)
    my_bookc('Kniga', 'I ewe kniga', 'Esli pos4itaew to bydet 3 knigi')
