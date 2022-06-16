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


class ShiftSupervisor(Employee):

    def __init__(self, name, number, salary, bonus):
        Employee.__init__(self, name, number)
        self.__anualSalary = salary
        self.__anualProdBonus = bonus

    def set_anual_salary(self, salary):
        self.__anualSalary = salary

    def get_anual_salary(self):
        return format(self.__anualSalary, ',.2f')

    def set_anual_bonus(self, bonus):
        self.__anualProdBonus = bonus

    def get_anual_bonus(self):
        return format(self.__anualProdBonus, ',.2f')
