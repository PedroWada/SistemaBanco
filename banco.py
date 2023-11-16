#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from class_Conta import ContaCorrente
from class_cliente import Cliente

# Sistema
def linha():
    print("-" * 30)
linha()
print("Sitema de Banco".center(30))
linha()
linha()
print("LOGIN".center(30))
linha()

Admin = False

with open("clientes.txt") as arq:
    encontrado1 = True
    clientes = arq.readlines()
    while encontrado1:
        cpf = str(input("Cpf: "))
        senha = str(input("Senha: "))
        for linha in clientes:
            lista = linha.split("#")
            if cpf == lista[3] and senha == lista[4]:
                if lista[0] == "Admin":
                    Admin = True
                    encontrado1 = False
                    break
                else:
                    print(f'Bem vindo! {lista[0]}')
                    usuario = Cliente(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5])
                    numeroConta = lista[5]
                    encontrado1 = False
                    break
        if encontrado1:
            print('Cpf ou senha invalidos!')

if Admin == False:
    with open("contas_correntes.txt") as arq:
        contas = arq.readlines()
        for linha in contas:
            lista = linha.split("#")
            print(lista)
            if numeroConta == lista[2]:
                conta = ContaCorrente(float(lista[0]), lista[1], lista[2])

if Admin:
    print('Bem Vindo Administrador! ')
    respondendo1 = True
    while respondendo1:
        opcao = int(input("\n"'''O que deseja fazer?
             1 - Adicionar Cliente
             2 - Remover Cliente
             3 - Ver Clientes
             4 - Ver Contas Correntes
             5 - Sair
         Opção: '''))
        if opcao == 1:
            nome = input("Nome do novo Cliente: ")
            dataNasc = input("Data de Nascimento: ")
            ende = input("Endereço: ")
            cpf = input("CPF: ")
            senha = input("Senha: ")
            numConta = input("numConta: ")

            novoCliente = Cliente(nome,dataNasc,ende,cpf,senha,numConta)
            novoCliente.adicionar()
            Saldo = float(input("Saldo da Conta: "))
            agencia = input("Código da Agencia: ")
            novaConta = ContaCorrente(Saldo, agencia, numConta)
            novaConta.adicionar()
            print("Cliente Adicionado com sucesso! ")

        elif opcao == 2:
            cpf = input("Cpf do cliente que deseja remover: ")
            with open('clientes.txt') as arq:
                clientes = arq.readlines()
                for i,linha in enumerate(clientes):
                    lista = linha.split("#")
                    if cpf == lista[3]:
                        print(lista[0])
                        clientes.pop(i)
            with open("clientes.txt", "w") as arq:
                arq.writelines(clientes)
                print("Cliente Removido com sucesso!")
        elif opcao == 3:
            with open('clientes.txt') as arq:
                clientes = arq.readlines()
                for linha in clientes:
                    print(linha)
        elif opcao == 4:
            with open('contas_correntes.txt') as arq:
                contas = arq.readlines()
                for linha in contas:
                    print(linha)
        elif opcao == 5:
            print("Programa finalizado! Até Breve")
            break
        else:
            print("Opção Invalida!")

else:
    respondendo = True
    while respondendo:
        opcao = int(input("\n"'''O que deseja fazer?
        1 - Saque
        2 - Depósito
        3 - Saldo
        4 - Pix
        5 - Meus Dados
        6 - Sair
    Opção: '''))

        if opcao == 1:
            valor = float(input(f"Quanto deseja sacar do seu saldo de {conta.saldo}? "))
            conta.saque(valor)
        elif opcao == 2:
            valor = float(input(f"Quanto deseja depositar? "))
            conta.deposito(valor)
        elif opcao == 3:
            conta.mostrar_saldo()
        elif opcao == 4:
            print('PIX')
            with open("clientes.txt", encoding="utf8") as arq:
                encontrado = True
                clientes = arq.readlines()
                while encontrado:
                    chave = str(input('Cpf do destinatario: '))
                    for linha in clientes:
                        lista = linha.split("#")
                        if chave == lista[3] and chave != cpf:
                            print('Cliente Encontrado!')
                            print("Nome: "+lista[0])
                            encontrado = False
                            break
                    if encontrado:
                        print('Cpf invalido!')
            valor = float(input("Quanto deseja transferir: "))
            conta.transferir(valor, chave)

        elif opcao == 5:
            usuario.mostrar_dados()
        elif opcao == 6:
            print("Obrigado! Até a próxima.")
            break
        else:
            print("Opção inválida, tente novamente.")