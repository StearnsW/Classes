class Book:
    """Book class"""
    def __init__(self,title):
        self.__title=title
        self.__author=""
        self.__copyright=-1
        self.__publisher=""
    
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def publiser(self):
        return self.__publisher

    @property
    def copyright(self):
        return self.__copyright

    @title.setter
    def title(self,new_title):
        self.__title=new_title

    @author.setter
    def author(self,new_author):
        self.__author=new_author

    @publiser.setter
    def publisher(self,new_publisher):
        self.__publisher=new_publisher

    @copyright.setter
    def copyright(self,new_copyright):
        self.__copyright=new_copyright
