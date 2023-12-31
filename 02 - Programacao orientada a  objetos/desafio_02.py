from abc import ABC, abstractmethod, abstractproperty
from datetime import date, datetime

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
     
    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            }
        )

class Conta():
    def __init__(self, numero: int, cliente, historico: Historico):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def numero(self) -> int:
        return self._numero
    
    @property
    def agencia(self) -> str:
        return self._agencia
    
    @property
    def historico(self) -> Historico:
        return self._historico    
    
    
    
    def sacar(self, valor: float):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print('\n#### Operação Falhou! saldo insuficiente. ####')
        
        elif valor > 0:
            self._saldo -= valor
            print('\n===Saque realizado com sucesso! ===')
            return True
        
        else:
            print('\n **** Operação falhou! o valor informado é inválido ****')
        
        return False   
    
    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print('\n === Deposito realizado com sucesso! ===')
            return True
        else:
            print('\n **** Operação falhou! O valor informado é inválido ****')
        
        return False
    
class Cliente:
    def __init__(self, endereco: str, contas: list):
        self.endereco = endereco
        self.contas = contas
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500.00, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor: float):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print('\n **** Operação falhou! o valor do saque excede o seu limite. ****')
        
        elif excedeu_saques:
            print('\n **** Operação falhou! Voce chegou ao seu limite de saques no dia. ****')
        
        else:
            return super().sacar(valor)   
    
class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
               
        