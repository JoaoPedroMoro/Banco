from typing import List
from time import sleep

from models.conta import Conta
from models.cliente import Cliente


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('---------- ATM ----------')
    print('--------- Banco ---------')

    print('Selecione uma opção no menu:')
    print('1 - Criar uma conta')
    print('2 - Efetuar um saque')
    print('3 - Efetuar um depósito')
    print('4 - Transferir para outra conta')
    print('5 - Listar contas existentes')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_trasnferencia()
    elif opcao == 5:
        listar_contas()
    else:
        print('Volte sempre :)')
        sleep(2)
        exit(0)


def criar_conta() -> None:
    print('Informe os dados do cliente: ')
    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, cpf, data_nascimento, email)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucecsso!')
    print('Dados da conta: ')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}.')
    else:
        print('Ainda não existem contas cadastradas. Voltando ao menu ...')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta para depósito: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}.')
    else:
        print('Ainda não existem contas cadastradas. Voltando ao menu ...')
    sleep(2)
    menu()


def efetuar_trasnferencia() -> None:
    if len(contas) > 0:
        numero_origem: int = int(input('Informe o número da conta de origem: '))
        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino: int = int(input('Informe o número da conta de destino: '))
            conta_destino: Conta = buscar_conta_por_numero(numero_destino)

            if conta_destino:
                valor: float = float(input('Informe o valor que vai ser transferido: '))

                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'Não foi encontrada a conta com número {numero_destino}.')
        else:
            print(f'Não foi encontrada a conta com número {numero_origem}.')
    else:
        print('Ainda não existem contas cadastradas. Voltando ao menu ...')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('--- Listagem de contas ---')
        for conta in contas:
            print(conta)
            print('--------------------')
            sleep(1)
        menu()
    else:
        print('Ainda não existem contas cadastradas. Voltando ao menu ...')
        sleep(2)
        menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta

    return c


if __name__ == '__main__':
    main()
