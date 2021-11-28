from Conta_corrente import *


def main():
    felipe_account = BankAccount('Felipe Stahl Silvestre', 5000, '001')
    felipe_credit = CreditCard('Felipe', felipe_account)
    print(felipe_credit.__dict__)
    print(felipe_account.client_info())


if __name__ == '__main__':
    main()