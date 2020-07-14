## Animal is-a object(是的，有点混乱) look at the extra credit.
class Animal(object):
    pass

#Dog is-a Animal.
class Dog(Animal):

    def __init__(self,name):
        #嘿，取个名
        self.name = name

#Cat is-a Animal.
class Cat(Animal):

    def __init__(self,name):
        #可爱的猫咪当然配拥有姓名
        self.name = name

#Person is-a object.
class Person(object):
    
    def __init__(self,name):
        self.name = name


        #Person has-a pet of some kind
        self.pet = None

#员工 is-a Person
class Employee(Person):
    
    def __init__(self,name,salary):
        ## ?? hmm what is this strange magic?
        super(Employee,self).__init__(name)
        ##??
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## satan是mary的一只宠物
mary.pet = satan

## frank是一位员工，薪水120000,(津巴布韦币，年薪)
frank = Employee("Frank",120000)

## rover是frank的一直宠物
frank.pet = rover

## 海豹是鱼的一种实例
flipper = Fish()

## crouse是鲑鱼的一个实例
crouse = Salmon()

## harry是大比目鱼的一个实例
harry = Halibut()