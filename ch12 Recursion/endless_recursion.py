from email import message


def main():
    message()

def message():
    print('This is a recursive function')
    message()

main()