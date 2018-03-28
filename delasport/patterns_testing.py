from abc import ABCMeta, abstractmethod
from copy import deepcopy

"""
SINGLETON pattern
"""


class Singleton(object):
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
        return cls._instance


class SingletonA(Singleton):
    pass


class SingletonB(Singleton):
    pass


class SingletonA1(SingletonA):
    pass


a = SingletonA()
a1 = SingletonA1()
b = SingletonB()

a.x = 100

print("{0} SINGLETON {0}".format('#'*10))

print(a.x)
print(a1.x)

print("{0} SINGLETON {0}".format('#'*10))

"""
SINGLETON pattern end
"""

"""
BORG pattern
"""


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

class IBorg(Borg):

    def __init__(self):
        Borg.__init__(self)
        self.state = 'init'

    def __unicode__(self):
        return self.state


class ABorg(Borg): pass


class BBorg(Borg): pass


class A1Borg(Borg): pass


a = ABorg()
a1 = A1Borg()
b = BBorg()

a.x = 100

print("{0} BORG {0}".format('#'*10))
print(a.x)
print(a1.x)
print(b.x)
print("{0} BORG {0}".format('#'*10))

"""
BORG pattern end
"""

"""
FACTORY pattern start
"""


class Employee(metaclass=ABCMeta):
    """ An Employee class """
    def __init__(self, name, age, gender):

        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return "{} - {}, {} years old {}".format(self.__class__.__name__,self.name,self.age,self.gender)


class Engineer(Employee):
    """ An Engineer Employee """
    def get_role(self):
        return "engineering"


class Accountant(Employee):
    """ An Accountant Employee """
    def get_role(self):
        return "accountant"


class Admin(Employee):
    """ An Admin Employee """
    def get_role(self):
        return "administration"


class EmployeeFactory(object):

    @classmethod
    def create(cls, name, *args):
        """ Factory method for creating an Employee instance """

        name = name.lower().strip()

        if name == 'engineer':
            return Engineer(*args)
        elif name == 'accountant':
            return Accountant(*args)
        elif name == 'admin':
            return Admin(*args)


engineer = EmployeeFactory.create('engineer', 'Gosho', '25', 'M')

print("{0} FACTORY {0}".format('#'*10))

print(engineer.get_role())

print("{0} FACTORY {0}".format('#'*10))
"""
FACTORY pattern end
"""


"""
PROTOTYPE pattern start
"""


class Prototype(object):

    def clone(self):
        return deepcopy(self)


class Register(Prototype):

    def __init__(self, names=[]):
        self.names = names

    def __str__(self):
        return ", ".join(self.names)

r1 = Register(names=["Lily", "Pesho", "Alex"])

r2 = r1.clone()
r2.names.append("Gosho")


class MetaPrototype(type):

    def __init__(cls, *args):
        type.__init__(cls, *args)
        cls.clone = lambda self: deepcopy(self)


class PrototypeM(metaclass=MetaPrototype): pass

class ItemCollection(PrototypeM):

    def __init__(self, items=[]):
        self.items = items

    def __str__(self):
        return ", ".join(self.items)


i1 = ItemCollection(items=['disc', 'video', 'floppy'])
i2 = i1.clone()

print(i2.items)

"""
PROTOTYPE pattern end
"""


"""
BUILDER pattern start
"""

# Using the Builder pattern to build Lego house with Rooms and Porch

class Room(object):

    def __init__(self, nwindows=2, doors=1, direction='S'):
        self.nwindows = nwindows
        self.ndoors = doors
        self.direction = direction

    def __str__(self):
        return "Romm <facing:{}, windows=#{}>".format(self.direction, self.nwindows)


class Porch(object):

    def __init__(self, ndoors=2, direction='W'):
        self.ndoors = ndoors
        self.direction = direction

    def __str__(self):
        return "Porch <facing:{}, doors=#{}>".format(self.direction, self.ndoors)


class LegoHouse(object):

    def __init__(self, nrooms=0, nwindows=0, nporches=0):
        # windows per room
        self.nwindows = nwindows
        self.nporches = nporches
        self.nrooms = nrooms
        self.rooms = []
        self.porches = []

    def __str__(self):
        msg = "LegoHouse<rooms=#{}, porches=#{}>".format(self.nrooms, self.nporches)

        for r in self.rooms:
            msg += str(r)

        for p in self.porches:
            msg += str(p)

        return msg

    def add_room(self, room):
        self.rooms.append(room)

    def add_porch(self, porch):
        self.porches.append(porch)


class LegoHouseBuilder(object):

    def __init__(self, *args, **kwargs):
        self.house = LegoHouse(*args, **kwargs)

    def build(self):

        self.build_rooms()
        self.build_porches()

        return self.house

    def build_rooms(self):

        for r in range(self.house.nrooms):
            room = Room(self.house.nwindows)
            self.house.add_room(room)

    def build_porches(self):

        for p in range(self.house.nporches):
            porch = Porch(1)
            self.house.add_porch(porch)


builder = LegoHouseBuilder(nrooms=2, nporches=1, nwindows=1)

print("{0} BUILDER {0}".format('#'*10))

print(builder.build())

print("{0} BUILDER {0}".format('#'*10))



"""
BUILDER pattern end
"""


def fibonacci():
    a,b = 0,1
    while True:
        yield b
        a,b = b, a+b

fib = fibonacci()

print(", ".join([str(next(fib)) for x in range(15)]))

def factoriel(n):
    if n == 0:
        return 1
    else:
        return n*factoriel(n-1)

fac = factoriel(5)
print(fac)


class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return "This is {}, aged {}".format(self.name, self.age)

class Medic(Person):
    def __init__(self, *args, **kwargs):
        super(Medic, self).__init__(*args, **kwargs)
        self.proffesion = 'medic'

    def __str__(self):
        return "This is {}, aged {}, with a {} profesion".format(self.name, self.age, self.proffesion)

m1 = Medic('Teodor', 45, 'M')
print(m1)