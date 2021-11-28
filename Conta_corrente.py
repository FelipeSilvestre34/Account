from datetime import datetime
from random import randint
from Angecia import Agency


class BankAccount:
    """
    Create a class for a bank account to manage clients accounts

    Attributes:
        _account (int): account number
        __agency (int): account agency
        firstname (str): client first name
        middlename (str): client middle name
        lastname (str): client last name
        __balance (float): __balance of the account
        credit (float): credit card of the client
        credit_limit (float): Limit of the credit card
        limit (float): the value that the client can have below 0
        max_limit (float): the max limit that the client can go below 0
        transactions (list): the historical transaction of the account
        _credit (list): a list with associated Credit Cards
    """

    @staticmethod
    def _date_time():
        return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, name: str, balance: float, agency: str):
        self._account = int(str(randint(1, 9)) + str(randint(0, 9)) + str(randint(0, 9))
                            + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)))
        self.full_name = name.split(' ')
        if len(self.full_name) == 2:
            self.firstname = self.full_name[0]
            self.lastname = self.full_name[1]
        else:
            self.firstname = self.full_name[0]
            self.middlename = self.full_name[1:-1]
            self.lastname = self.full_name[-1]
        self.agency = agency
        self.__balance = balance
        self.limit = balance * 0.2
        self.__max_limit = balance * 0.2
        self.transactions = []
        self.credit_card = []


    def client_info(self):
        print(f'Nome Completo: {" ".join(self.full_name)}\n'
              f'Número da conta: {self._account}\n'
              f'Número da Agência: {self.agency}\n')

    def check_balance(self):
        print(f'O Saldo em sua conta é de: R${self.__balance:,.2f}')

    def check_limit(self):
        print(f'O Limite em sua conta é de: R${self.limit:,.2f}')

    def check_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def _check_limit(self):
        return self.limit

    def withdraw(self, withdraw_value: float):
        if self.__balance > 0 and withdraw_value <= self.__balance:
            self.__balance -= withdraw_value
            print(f'Valor Sacado: R${withdraw_value:,.2f}\n'
                  f'O seu saldo é de: R${self.__balance}')
        elif 0 < self.__balance < withdraw_value:
            temp = withdraw_value
            temp -= self.__balance
            self.__balance = 0
            self.__balance -= temp
            self.limit -= temp
            print(f'Valor Sacado: R${withdraw_value:,.2f}\n'
                  f'O seu saldo é de: R${self.__balance}\n'
                  f'O seu limite é de: R${self.limit}')
        elif self.__balance <= 0:
            if self._check_limit() > 0 and withdraw_value < self._check_limit():
                self.__balance -= withdraw_value
                self.limit -= withdraw_value
                print(f'Valor Sacado: R${withdraw_value:,.2f}\n'
                      f'O seu saldo é de: R${self.__balance}\n'
                      f'O seu limite é de: R${self.limit}')
            else:
                print(f'{self.name} está sem limite e saldo em conta para este saque')
        self.transactions.append((-withdraw_value, self.__balance, BankAccount._date_time()))

    def deposit(self, deposit_value: float):
        if self.__balance > 0:
            self.__balance += deposit_value
        if self.__balance <= 0:
            self.limit += deposit_value
            self.__balance += deposit_value
            if self.limit > self.__max_limit:
                self.limit = self.__max_limit
        self.transactions.append((deposit_value, self.__balance, BankAccount._date_time()))

    def increase_limit(self, new_limit: float):
        if self.__balance < 0:
            return f'O Saldo em sua Conta é de: R${self.__balance:,.2f}, novo limite não autorizado'
        elif new_limit < self.__balance * 0.4 and self.__balance > 0:
            if self._check_limit() == self.__max_limit:
                self.limit += new_limit
                self.__max_limit = self.limit
                return f'O novo limite é de: R${self.limit:,.2f} now!'
        else:
            return 'Limite não autorizado'

    def transfer(self, transfer_value: float, transfer_account):
        if self.__balance >= transfer_value:
            self.__balance -= transfer_value
            self.transactions.append((-transfer_value, self.__balance, BankAccount._date_time()))
            transfer_account.deposit(transfer_value)
            print(f'O valor transferido foi de: R${transfer_value:,.2f}\n'
                  f'Transferencia da conta: {self.account} para a conta: {transfer_account.account}')

    def limit_credit(self):
        return self.__balance


class CreditCard:
    """
        Create a class for a credit card

        Attributes:
            name (str): credit card user name
            _number (int): credit card 16 digits number
            expiration_date (date) : credit card expiration date
            _limit (float): credit card limit
            _password: credit card password
            _bank_account: insert basic info from the credit card into the user's Bank Account class
        """

    @staticmethod
    def _date_time():
        return datetime.now()

    def __init__(self, name: str, bank_account):
        self.name = name
        self.number = f'{randint(1000, 9999)} {randint(1000, 9999)} {randint(1000, 9999)} {randint(1000, 9999)}'
        self.expiration_date = f'{CreditCard._date_time().month}/{CreditCard._date_time().year + 4}'
        self._security_code = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self._limit = (bank_account.limit_credit() * 0.3)
        self._password = f'{str(randint(1000,9999))}'
        self.__block = False
        self._bank_account = bank_account
        bank_account.credit_card.append({self.number: [self.expiration_date, self.name, self._limit]})


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        tries = 0
        if not self.__block:
            while tries < 4:
                value = input('Inserir nova senha: ')
                if len(value) == 4 and value.isnumeric():
                    self._password = value
                    print('Senha Atualizada')
                    break
                else:
                    print(f'Senha Invalida, favor inserir nova senha você tem {3-tries} tentativas')
                tries += 1
            else:
                self.__block = True
                print('Troca de senha bloqueada')
        else:
            print('Entrar em contato com o setor administrativo')



