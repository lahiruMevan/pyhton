
import bankaccount2

def main():
    start_bal = float(input('Enter your staring balace: '))

    savings = bankaccount2.Bankaccount(start_bal)

    pay = float(input('How much were you paid this week?'))
    print('I will deposit that into your account.')
    savings.deposit(pay)

    print(savings)

    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw  that from your account.')
    savings.withdraw(cash)

    print(savings)


main()


