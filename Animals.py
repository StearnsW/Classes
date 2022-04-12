class Animal:
    """Animal Class"""
    def __init__(self,species):
        self.__species=species
        self.__color="Unknown"
    
    @property
    def species(self):
        return self.__species
    
    @property
    def color(self):
        return self.__color

    @species.setter
    def species(self,new_species):
        self.__species=new_species
    
    @color.setter
    def color(self,new_color):
        self.__color=new_color

    def move(self):
        print("Moving")

    def sleep(self):
        print("Sleeping")





class Person(Animal):
    """Person class, inheriting from Animal"""
    def __init__(self,name):
        Animal.__init__(self,"Human")
        self.__name=name
    
    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return "Nope, not for people"

    @name.setter
    def name(self,new_name):
        self.__name=new_name

    def talking(self):
        print("Chatting up a storm.")


class Snake(Animal):
    """Snake class, inheriting from Animal"""
    @property
    def ID_Number(self):
        return self.__idnum

    @ID_Number.setter
    def ID_Number(self, num):
        self.__idnum=num

    def hiss(self):
        print("Doing that tounge thing")


class Fish(Animal):
    """Fish class, inheriting from Animal"""
    def swim(self):
        print("Just keep swimming")

    def destination(self):
        print("P Sherman 42 Wallaby Way Sydney")