import pickle
phonebook = {'Chris': '555-1111',
              'Katie': '555-2222', 'Joanne':'555-3333'}

output_file = open('phonebook.dat', 'wb')
pickle.dump(phonebook, output_file)
output_file.close()

input_file = open('phonebook.dat', 'rb')
pb = pickle.load(input_file)
print(pb)
input_file.close()
