#INHERITANCE
class Animal:
    def __init__(self):
        print("ANIMAL CREATED");
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("EATING")


#mya = Animal()
#mya.whoAmI()
#mya.eat()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")
    def bark(self):
        print("Woof!")
    def eat(self):
        print("DOG EATING")

myd = Dog()
myd.eat()
myd.whoAmI()
myd.bark()


#Special Methods
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = int(pages)
    def __str__(self):
        return self.title+" "+self.author+" "+str(self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book has been destroyed")

b = Book('Python',"Dipo","1024")
print(b)
print(len(b))

# delete object
del b
