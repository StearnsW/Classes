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


class Car(Vehicle):
    """Car class, inheriting from Vehicle"""
    def __init__(self,make,model):
        Vehicle.__init__(self,"car")
        Vehicle.make=make
        Vehicle.model=model
        Vehicle.number_wheels=4


class Boat(Vehicle):
    """Boat class, inheriting from Vehicle"""
    def __init__(self,make,model):
        Vehicle.__init__(self,"boat")
        Vehicle.make=make
        Vehicle.model=model
        Vehicle.number_wheels=0
        self.__floats=True

    @property
    def floats(self):
        return self.__floats

    @floats.setter
    def floats(self,float_bool):
        self.__floats=float_bool


class Bicycle(Vehicle):
    """Bicycle class, inheriting from Vehicle"""
    def __init__(self,make,model,kickstand_bool):
        Vehicle.__init__(self,"bicycle")
        Vehicle.make=make
        Vehicle.model=model
        Vehicle.number_wheels=2
        self.__kickstand=kickstand_bool

    @property
    def has_kickstand(self):
        return self.__kickstand

    @has_kickstand.setter
    def has_kickstand(self,kickstand_bool):
        self.__kickstand=kickstand_bool

    def reverse():
        print("not a viable option for this vehicle")


class HotAirBaloon(Vehicle):
    """HotAirBaloon class, inheriting from Vehicle"""
    def __init__(self):
        Vehicle.__init__(self,"hot air baloon")
        self.__tied=True
    
    @property
    def tied_down(self):
        return self.__tied

    @tied_down.setter
    def tied_down(self,tied_bool):
        self.__tied=tied_bool

    def move(self):
        if self.__tied:
            print("The baloon is tied down and can't move")
        else:
            print("We can see everyting here in the sky")
    
    def reverse(self):
        if self.__tied:
            print("The baloon is tied down and can't move")
        else:
            print("We're at the mercy of the wind, plans are meaningless")
        
    def take_off(self):
        if self.__tied:
            print("The baloon is tied down and can't move")
        else:
            print("Taking Off")

    def land(self):
        if self.__tied:
            print("The baloon is already on the ground")
        else:
            print("Landing")