import pickle
import cellphone

FILENAME = 'cellphone.dat'

def main():
    again = 'y'

    output_file = open(FILENAME, 'wb')

    while again.lower() == 'y':
        man = input('Enter the manufacture: ')
        mod = input('Enter the model number: ')
        retail = float(input('Enter the retail price: '))

        phone = cellphone.CellPhone(man, mod, retail)

        pickle.dump(phone, output_file)

        again = input('Enter more phones data? (y/n): ')

    output_file.close()
    print('The data waas written to ',FILENAME)

main()


