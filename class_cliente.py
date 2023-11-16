
class Cliente:
    def __init__(self, nome,dataNasc,endereco,  cpf, Senha, numeroConta):
        self.nome = nome
        self.dataNasc = dataNasc
        self.endereco = endereco
        self.cpf = cpf
        self.senha = Senha
        self.numeroConta = numeroConta

    def adicionar(self):
        with open("clientes.txt", "a") as arq:
            arq.write(f"{self.nome}#{self.dataNasc}#{self.endereco}#{self.cpf}#{self.senha}#{self.numeroConta}")

    def mostrar_dados(self):
        print(f"Nome: {self.nome} / CPF: {self.cpf} / Data de Nascimento: { self.dataNasc} / "
              f"Numero da Conta: {self.numeroConta} / Endereço: {self.endereco}")
