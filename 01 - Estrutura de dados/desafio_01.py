import os
import time
import textwrap


def menu():
    menu = '''
    ##Bem vindo ao Banco PyBank##
    Escolha uma das opções abaixo:
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
=>'''
    
    return input(textwrap.dedent(menu))



def limpa_console(opcao, reposta):
    if reposta == 'v':
        os.system('clear')
        opcao

def depositar(saldo, valor, extrato, limpa_console, opcao, /):
    if valor > 0:
        saldo += valor
        extrato +=f'Deposito:  R${saldo:.2f}\n'
            
        reposta = input( 
                        f'''
                            Valor depositado foi de R${saldo:.2f}
                            aperte a tecla [v] para voltar ao menu
                        '''
                    )
            
        limpa_console(opcao, reposta)
        return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, LIMITE_SAQUES, limpa_console, opcao): #TODO
    
    if LIMITE_SAQUES > 0:
        if int(valor) <= limite:
            if saldo < int(valor):
                reposta = input( 
                                f'''
                                    saldo insuficiente.
                                    aperte a tecla [v] para voltar ao menu
                                '''
                            )
            else:
                saldo -= int(valor)
                    
                reposta = input( 
                                f'''
                                    Valor sacado foi de R${float(valor):.2f}, saldo atualizado para R${saldo:.2f}
                                    aperte a tecla [v] para voltar ao menu
                                '''
                            )
                LIMITE_SAQUES -= 1
            extrato += f'\t\tSaque:  R${float(valor):.2f}\n\t\tSaldo Atualizado: R${saldo:.2f}\n'
            limpa_console(opcao, reposta)
                    
        else:
            print(f'SAQUE BLOQUEADO!!! (O limite de saque para a sua conta é R${limite})')
            time.sleep(2)
            os.system('clear')
            opcao
    else:
        print(f'Voce chegou ao limite de saques por dia')
        time.sleep(2)
        os.system('clear')
        opcao

def exibe_extrato(extrato, /, limpa_console, * , opcao):
    if extrato != '':
        print(
                f'''
                ###############################################
                	Voce ja pode ver o seu saldo no PyBank
                ###############################################
                {extrato}
                ''')
        reposta = input(
                '''
                aperte a tecla [v] para voltar ao menu
                '''
            )
        limpa_console(opcao,reposta)       
            
            
    else:
        print('Não houve movimentações na sua conta\n Suporte Pybank')
        time.sleep(2)
        os.system('clear')
        opcao
        
        
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = menu()

    if opcao == 'd':
        os.system('clear')
        valor = float(input(
            '''
            ###############################################
              Voce ja pode fazer o seu deposito no PyBank
            ###############################################
            Digite o valor que deseja depositar: 
            '''
        ))
        saldo, extrato = depositar(saldo, valor, extrato, limpa_console, opcao)
    
    elif opcao == 's':
        os.system('clear')
        valor = input(
            '''
            ###############################################
              Voce ja pode fazer o seu saque no PyBank
            ###############################################
            Digite o valor que deseja sacar: 
            '''
        )
        saldo, extrato = sacar(saldo, valor, limite, extrato, LIMITE_SAQUES, limpa_console, opcao)
                    
    elif opcao == 'e':
        exibe_extrato(extrato, limpa_console, opcao)
            
    elif opcao == 'q':
        break
    
    else:
        print("Operação Invalida, por favor selecione novamente a operação desejada.")
                
                
            
            
                
            
    
