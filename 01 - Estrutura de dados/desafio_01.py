import os
import time
import textwrap


def menu():
    menu = '''
    ##Bem vindo ao Banco PyBank##
    Escolha uma das opções abaixo:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] tNovo usuário
    [q] Sair
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

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, limpa_console, opcao): 
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        reposta = input( 
                        f'''
                            saldo insuficiente.
                            aperte a tecla [v] para voltar ao menu
                        '''
                        )
        limpa_console(opcao, reposta)
    elif excedeu_limite:
        print(f'SAQUE BLOQUEADO!!! (O limite de saque para a sua conta é R${limite})')
        time.sleep(2)
        os.system('clear')
        opcao
        
    elif excedeu_saques:
        print(f'Voce chegou ao limite de saques por dia')
        time.sleep(2)
        os.system('clear')
        opcao
    
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
                    
        reposta = input( 
                        f'''
                            Valor sacado foi de R${valor:.2f}, saldo atualizado para R${saldo:.2f}
                            aperte a tecla [v] para voltar ao menu
                        '''
                    )
                
        extrato += f'\t\tSaque:  R${float(valor):.2f}\n\t\tSaldo Atualizado: R${saldo:.2f}\n'
        limpa_console(opcao, reposta)
        
    else:
        print('\t\t###Falha na operação! O Valor informado é inválido.###')
        
    return saldo, extrato

def exibe_extrato(extrato, /, limpa_console, * , opcao):
    if extrato != '':
        print(
                f'''
                ###############################################
                	Voce ja pode ver o seu saldo no PyBank
                ###############################################
                {extrato}\n
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

def criar_usuario(usuarios):
    cpf = input('\tInforme o seu CPF para se cadastrar (Digite somente os números)')
    
    usuario = filtrar_usuario(usuarios, cpf)
    
    if usuario:
        print('\t\t### Já existe usuário com esse CPF! ###')
    
    nome = input('Digite o nome completo: ')
    data_nascimento = input('Digite o data_nascimento: ')
    endereco = input('Informe o endereço(logradouro, numero - bairro - cidade/sigla estado) : ')       
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco})
    
def filtrar_usuario(usuarios, cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('\tInforme o seu CPF para se cadastrar (Digite somente os números)')
    
    usuario = filtrar_usuario(usuarios, cpf)
    
    if usuario:
        print('\n === Conta criada com suceso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}    
    
    print('\n ### Usuário não encontrado, Fluxo de criação de conta encerrado! ###')
    
def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            Id_Conta:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))
        
        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

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
            valor = float(input(
            '''
            ###############################################
              Voce ja pode fazer o seu saque no PyBank
            ###############################################
            Digite o valor que deseja sacar: 
            '''
            ))
            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                limpa_console=limpa_console,
                opcao=opcao,
            )
                    
        elif opcao == 'e':
            exibe_extrato(extrato, limpa_console=limpa_console, opcao=opcao)
            
        elif opcao == 'q':
            break
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        
        else:
            print("Operação Invalida, por favor selecione novamente a operação desejada.")
            time.sleep(3)
            os.system('clear')

main()
                
                
            
            
                
            
    
