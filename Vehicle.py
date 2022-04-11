class Vehicle:
    """Vehicle class"""
    def __init__(self,vehicle_type):
        self.__type=vehicle_type
        self.__make=""
        self.__model=""
        self.__color=""
        self.__model_year=-1
        self.__number_wheels=-1
   
    @property
    def type(self):
        return self.__type

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def model_year(self):
        return self.__model_year

    @property
    def color(self):
        return self.__color

    @property
    def number_wheels(self):
        if self.__number_wheels==-1:
            return None
        else:
            return self.__number_wheels

    @type.setter
    def type(self,new_type):
        self.__type=new_type

    @make.setter
    def make(self,new_make):
        self.__make=new_make

    @model.setter
    def model(self,new_model):
        self.__model=new_model

    @model_year.setter
    def model_year(self,new_model_year):
        self.__model_year=new_model_year

    @color.setter
    def color(self,new_color):
        self.__color=new_color

    @number_wheels.setter
    def number_wheels(self,new_number_wheels):
        self.__number_wheels=new_number_wheels

    def move():
        print("Moving forward")

    def reverse():
        print("Moving backwards")


