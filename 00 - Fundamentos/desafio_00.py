import os
import time


menu = '''
    ##Bem vindo ao Banco PyBank##
    Escolha uma das opções abaixo:

    [d] Depositar
    [s] sacar
    [e] Extrato
    [q] Sair

=>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

def limpa_console(opcao, reposta):
    if reposta == 'v':
        os.system('clear')
        opcao

while True:
    
    opcao = input(menu)

    if opcao == 'd':
        os.system('clear')
        deposito = input(
            '''
            ###############################################
              Voce ja pode fazer o seu deposito no PyBank
            ###############################################
            
            Digite o valor que deseja depositar: 
            '''
        )
        saldo = int(deposito)
        extrato +=f'Deposito:  R${saldo:.2f}\n'
        
        reposta = input( 
                    f'''
                    
                        Valor depositado foi de R${saldo:.2f}
                        
                        aperte a tecla [v] para voltar ao menu
                    '''
                )
        
        limpa_console(opcao, reposta)
    
    elif opcao == 's':
        os.system('clear')
        saque = input(
            '''
            ###############################################
              Voce ja pode fazer o seu saque no PyBank
            ###############################################
            
            Digite o valor que deseja sacar: 
            '''
        )
        if LIMITE_SAQUES > 0:
            if int(saque) <= limite:
                if saldo < int(saque):
                    reposta = input( 
                                f'''
                                
                                    saldo insuficiente.
                                    
                                    
                                    aperte a tecla [v] para voltar ao menu
                                '''
                            )
                else:
                    saldo -= int(saque)
                    
                    reposta = input( 
                                f'''
                                
                                    Valor sacado foi de R${float(saque):.2f}, saldo atualizado para R${saldo:.2f}
                                    
                                    
                                    aperte a tecla [v] para voltar ao menu
                                '''
                            )
                    LIMITE_SAQUES -= 1
                extrato += f'\t\tSaque:  R${float(saque):.2f}\n\t\tSaldo Atualizado: R${saldo:.2f}\n'
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
                    
    elif opcao == 'e':
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
            
    elif opcao == 'q':
        break
    
    else:
        print("Operação Invalida, por favor selecione novamente a operação desejada.")
                
                
            
            
                
            
    
