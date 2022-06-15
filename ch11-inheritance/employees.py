class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_employee_name(self, name):
        self.__name = name

    def get_employee_name(self):
        return self.__name

    def set_employee_number(self, number):
        self.__number = number

    def get_employee_number(self):
        return self.__number


class ProductionWorker(Employee):

    def __init__(self, name, number, shiftNum, hourly):
        Employee.__init__(self, name, number)
        self.__shiftNum = shiftNum
        self.__hourly = hourly

    def set_hourly_rate(self, houry):
        self.__hourly = houry

    def get_hourly_rate(self):
        return self.__hourly

    def set_shift(self, shiftNum):
        self.__shiftNum = shiftNum

    def get_shift(self):
        return self.__shiftNum
