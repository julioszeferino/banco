from multiprocessing import cpu_count
from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    '''
    Funcao que mostra um menu para o usuario e executa acoes de acordo com a opcao selecionada por ele.
    '''
    print('===================================')
    print('============== ATM ================')
    print('============== Bank ===============')
    print('===================================')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opcao inválida. Tente novamente, por favor.')
        sleep(2)
        menu()


def criar_conta() -> None:
    '''
    Funcao que solicita ao usuario os dados do cliente a ser cadastrado, criar o objeto cliente,
    associa uma conta a ele e adiciona a lista de contas.
    '''
    print('Informe os dados do cliente: ')

    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente (ex: 01/05/1999): ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('----------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    '''
    Funcao que verifica se ja existem contas cadastradas. Caso positivo, pede ao usuario que informe
    o numero da sua conta, se encontrada solicita um valor para o saque e executa a acao sacar.
    '''
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')

    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    '''
    Funcao que verifica se ja existem contas cadastradas. Caso positivo, pede ao usuario que informe
    o numero da sua conta, se encontrada solicita um valor para o deposito e executa a acao depositar.
    '''
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    '''
    Funcao que verifica se ja existem contas cadastradas. Caso positivo, pede ao usuario que informe
    o numero da conta de destino da transferencia, caso encontrada, solicita o valor da transferencia
    e executa a acao transferir.
    '''
    if len(contas) > 0:
        # verificando se a conta do usuario existe
        numero_origem: int = int(input('Informe o número da sua conta: '))
        conta_origem: Conta = buscar_conta_por_numero(numero_origem)
        # caso a conta do usuario exista, verificar a conta de destino
        if conta_origem:
            numero_destino: int = int(input('Informe o número da sua conta: '))
            conta_destino: Conta = buscar_conta_por_numero(numero_destino)
            # caso a conta de destino exista, executar a operacao de transferencia
            if conta_destino:
                valor: float = float(input('Informe o valor da transferencia: '))
                conta_origem.transferir(conta_destino, valor)
            else:
                 print(f'A conta de destino com número {numero_destino} não foi encontrada.')
        else:
            print(f'A sua conta com número {numero_origem} não foi encontrada.')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()

    
def listar_contas() -> None:
    '''
    Funcao que verifica se ja existem contas cadastradas. Caso positivo, imprime todas as contas
    cadastradas.
    '''
    if len(contas) > 0:
        print('Listagem de contas: ')
        
        for conta in contas:
            print(conta)
            print('--------------------')
            sleep(1)
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    '''
    Funcao que varre a lista de contas a procura de uma correspondencia.

    :params numero: o numero da conta pesquisada.
    :return: caso encontrada, retorna o objeto Conta correspondente ao numero.
    '''
    c = Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()