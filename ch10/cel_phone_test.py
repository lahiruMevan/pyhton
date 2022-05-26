import cellphone

def main():
    man = input('Enter the manufacture:')
    mod = input('Enter the model number:')
    retail = float(input('Enter the retail price:'))


    phone = cellphone.CellPhone(man, mod, retail)

    print('Here ih the data that was entered:')
    print('Manufacture:', phone.get_manufact())
    print('Model number:',phone.get_model())
    print('Retail Price: $', format(phone.get_retail_price(),',.2f'), sep='')

main()