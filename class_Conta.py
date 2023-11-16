class ContaCorrente:
    def __init__(self, saldo, numeroAgencia, num):
        self.saldo = saldo
        self.numeroAgencia = numeroAgencia
        self.num = num

    def saque(self, valor):
        if valor > self.saldo:
            print("\nNão foi possível realizar a operação. Valor maior que o disponível em saldo.")
        else:
            self.saldo -= valor
            with open('contas_correntes.txt', "r") as arq:
                contas = arq.readlines()
                for i,linha in enumerate(contas):
                    lista = linha.split("#")
                    if self.num == lista[2]:
                        linha = f'{self.saldo}#{self.numeroAgencia}#{self.num}'
                        contas[i] = linha
            with open("contas_correntes.txt", "w") as arq:
                arq.writelines(contas)

            print(f"\nO valor de {valor} foi sacado, novo saldo: {self.saldo}")

    def deposito(self, valor):
        if valor < 0 or valor == 0:
            print(f"\nNão foi possível realizar a operação. Valor inválido ou insuficiente.")
        else:
            self.saldo += valor
            with open('contas_correntes.txt', "r") as arq:
                contas = arq.readlines()
                for i, linha in enumerate(contas):
                    lista = linha.split("#")
                    if self.num == lista[2]:
                        linha = f'{self.saldo}#{self.numeroAgencia}#{self.num}'
                        contas[i] = linha
            with open("contas_correntes.txt", "w") as arq:
                arq.writelines(contas)
            print(f"\nO valor de {valor} foi depositado, novo saldo: {self.saldo}")

    def adicionar(self):
        with open("contas_correntes.txt", "a") as arq:
            arq.write(f"{self.saldo}#{self.numeroAgencia}#{self.num}")

    def transferir(self, valor, chave):
        if valor < 0 or valor == 0:
            print(f"\nNão foi possível realizar a operação. Valor inválido ou insuficiente.")
        elif valor > self.saldo:
            print("\nNão foi possível realizar a operação. Valor maior que o disponível em saldo.")
        else:
            self.saque(valor)
            with open("clientes.txt") as arq:
                clientes = arq.readlines()
                for linha in clientes:
                    lista = linha.split("#")
                    if chave == lista[3]:
                        numeroConta = lista[5]
                        break
            with open('contas_correntes.txt', "r") as arq:
                contas = arq.readlines()
                for i,linha in enumerate(contas):
                    lista = linha.split("#")
                    if numeroConta == lista[2]:
                        linha = f'{float(lista[0]) + valor}#{lista[1]}#{lista[2]}'
                        contas[i] = linha
            with open("contas_correntes.txt", "w") as arq:
                arq.writelines(contas)
            print(f'\n Pix efetuado com sucesso! \n No valor de: {valor} reais')

    def mostrar_saldo(self):
        print(f"\nO seu saldo atual é de {self.saldo} reais.")