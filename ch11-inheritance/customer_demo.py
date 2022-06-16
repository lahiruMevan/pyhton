import persons


def main():
    customer = persons.Customer(
        'testcustomer', '233 hdhdhdgd dhdhd djdjh', '99383839', 343)

    print('name: ', customer.get_name())
    print('address: ', customer.get_address())
    print('phone: ', customer.get_phone())
    print('customer id: ', customer.get_id())
    print('mailing list: ', customer.get_mail_list())


main()
