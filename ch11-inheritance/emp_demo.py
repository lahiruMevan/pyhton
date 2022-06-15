import employees


def make_list():
    emp_list = []

    print('Enter data for five employees')
    for count in range(1, 6):
        print('Employee ', count)
        name = input('Enter name :')
        num = input('Enter number :')
        shift_num = input('Enter shift number :')
        hourlyRate = float(input('enter hourly rate :'))

        temp = employees.ProductionWorker(name, num, shift_num, hourlyRate)

        emp_list.append(temp)

    return emp_list


def emp_Info(list):
    for item in list:
        print('Name :', item.get_employee_name())
        print('Number :', item.get_employee_number())
        print('Shift :', item.get_shift())
        print('rate :', item.get_hourly_rate())
        print()


def main():

    emp_list = make_list()
    emp_Info(emp_list)


main()
