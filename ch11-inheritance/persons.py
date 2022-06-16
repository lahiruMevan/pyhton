class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__telephone = phone

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_phone(self, number):
        self.__telephone = number

    def get_phone(self):
        return self.__telephone


class Customer(Person):

    def __init__(self, name, address, phone, id, mailing_list=True):
        Person.__init__(self, name, address, phone)
        self.__id = id
        self.__mailing_list = mailing_list

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_mail_list(self, status=True):
        self.__mailing_list = status

    def get_mail_list(self):
        return self.__mailing_list
