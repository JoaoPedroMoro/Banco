# Banco
Simulação de um aplicativo bancário. Aqui, o usuário pode criar uma conta nova, efetuar um saque, depósito ou transferência e listar as contas existentes no sistema.
Há 5 arquivos totais, sendo eles:

## teste.py
É o código para testar a criação dos objetos para checar se estão sendo criados da maneira correta.

## helper.py
Possui as funções de formatação, seja de string para data ou vice-versa, ou para ajustar a notação do dinheiro, que inicialmente é o modelo americano, para o modelo brasileiro.

## cliente.py
Cria o objeto cliente e suas propriedades, que são utilizadas pelo código principal.

## conta.py
Cria o objeto conta e suas propriedades, que são utilizadas pelo código principal.

## banco.py
É a aplicação do banco, o código principal. Nela é iniciado o sistema e contem todas as ações dele, que são:
- menu:
Mostra o menu de opções do sistema.
- main:
Chama a função menu.
- criar_conta:
Criação do cliente e da conta e adição dela na lista de contas do sistema.
- efetuar_saque:
Realização de um saque de uma determinada conta.
- efetuar_deposito:
Realização de um depósito de uma determinada conta.
- efetuar_transferencia:
Realização de uma transferência de uma conta origem para uma conta destino.
- listar_contas:
Mostra todas as contas cadastradas no sistema e suas informações.
- busca_conta-por_numero:
Função de auxílio das demais funções para resgatar uma conta a partir do número dela.
