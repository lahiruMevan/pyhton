import employees


def main():
    sp = employees.ShiftSupervisor('employeeTest', 434, 80000, 20000)

    print('name: ', sp.get_employee_name())
    print('number: ', sp.get_employee_number())
    print('salary: ', sp.get_anual_salary())
    print('bonus: ', sp.get_anual_bonus())


main()
