from utils.helper import date_para_str, str_para_date
from models.cliente import Cliente
from models.conta import Conta

teste1 = str_para_date('30/01/2024')

teste2 = date_para_str(teste1)

print(teste1)
print(teste2)

joao: Cliente = Cliente('João', '123.456.789-0', '16/09/1998', 'joao@gmail.com')
luiza: Cliente = Cliente('Luiza', '098.765.432-1', '10/04/1999', 'luiza@gmail.com')

print(joao)  # printando o __str__
print(luiza)

contaj: Conta = Conta(joao)
contal: Conta = Conta(luiza)

print(contaj)  # printado o __str__
print(contal)