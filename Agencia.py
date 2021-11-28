from Conta_corrente import BankAcconut, CreditCard


class Agency:

    def __init__(self, telefone: str, cnpj: str, numero: str):
        self.phone = phone
        self._cnpj = cnpj
        self.number = number
        self.clients = []
        self.__reserve = 0
        self._loans = []

    def check_reverse(self):
        if self.reserve < 1_000_000:
            print(f'Saldo em caixa abaixo do recomendado, caixa atual em: R${self.reserve:,.2f}')
        else:
            print(f'O saldo em caixa está em: R${self.reserve:,.2f}')

    def loan(self, value, cpf, fees):
        if self.__reserve > value:
            self.loans.append((value, cpf, fees))
        else:
            print('Emprestimo ainda não possivel')

    def add_client(self, name, cpf, patrimony):
        self.clients.append({nome: name, cpf:cpf, patrimonio:patrimony})


class OnlineAngecy(Agency):

    def __init__(self, telefone: str, cnpj: str, numero: str, local: url):
        super().__init__(telefone, cnpj, numero)
        self.local = local


class StreetAngecy(Agency):

    def __init__(self, telefone: str, cnpj: str, numero: str, address: url):
        super().__init__(telefone, cnpj, numero)
        self.address = address


class PremiunAngecy(Agency):

    def __init__(self, telefone: str, cnpj: str, numero: str, address: url):
        super().__init__(telefone, cnpj, numero)
        self.address = address