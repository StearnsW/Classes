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


class Textbook(Book):
    """Textbook class, inheriting from Book"""
    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self,new_subject):
        self.__subject=new_subject


class AddressBook(Book):
    """AddressBook class, inheriting from Book"""
    @property
    def number_addresses(self):
        return self.__numadds

    @number_addresses.setter
    def number_addresses(self,num):
        self.__numadds=num