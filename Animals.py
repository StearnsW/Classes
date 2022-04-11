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