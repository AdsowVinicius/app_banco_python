import os
import time

x = 1; i = 0
extrato = {}


def extratoConta(extrato, saldo):
    for chave, valor in extrato.items():
        print(f'ID {chave}: {valor[0]} no valor de R${valor[1]}')

    return menu(saldo)
        

def limpar():
    time(5)
    os.syste("cls")

def deposito(saldo):
    global x
    _valor = int(input("qual valor voce deseja depositar?"))              
    saldo += _valor
    extrato[x] = ["deposito", _valor]
    x += 1
    print(saldo)

    return menu(saldo)


def saque(saldo):
    global x, i
    i += 1

    print(saldo)
    _valor = int(input("qual valor voce deseja sacar?"))              
    if _valor > saldo :
        print("saldo insuficiente, faça um deposito para continuar sacando.")
        
    if i >= 3:
        print("limite de saque foi atingido")
        return False
        
    else:
        saldo -= _valor
        extrato[x] = ["saque", _valor]
        x += 1
        print(saldo)

    return menu(saldo)

def imprimirMenu():    
    print("""qual operação você dejesa realizar ?
                    1 ---->  Saque
                    2 ---->  Deposito
                    3 ---->  Visualizar extrato 
                    4 ---->  Sair
                    """)


def menu(saldo):
    imprimirMenu()
    validador(input(), saldo)
    



def validador(alternativa,saldo):
     while alternativa != "4":

        if alternativa == "1":
            saldo = saque(saldo)
        
        if saldo == False:
            menu()

        if alternativa == "2":
            saldo = deposito(saldo)
        
        if alternativa == "3":
            extratoConta(extrato, saldo)
        
        if alternativa == "4":
            break
      
    
    
    

    




    

    
