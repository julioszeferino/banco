from models.cliente import Cliente
from models.conta import Conta

julio: Cliente = Cliente('Julio Zeferino', 'julio@gmail.com', '139.424.046-23', '28/05/1998')
paulo: Cliente = Cliente('Paulao', 'paulo@mail.com', '124.788.956-68', '02/09/1995')

print(julio)
print(paulo)

conta1 : Conta = Conta(julio)
conta2 : Conta = Conta(paulo)

print(conta1)
print(conta2)