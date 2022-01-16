from models.cliente import Cliente
from utils.helper import formata_float_str_moeda

class Conta:
    codigo: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor
    
    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def __str__(self: object) -> str:
        return f'Número da Conta: {self.numero} \nCliente: {self.cliente.nome} \nSaldo Total: {formata_float_str_moeda(self.saldo_total)}'

    
    def depositar(self: object, valor: float) -> None:
        '''
        Funcao que recebe um valor de deposito. Atualiza os valores de saldo e do 
        saldo total (saldo + limite)

        :params valor: o valor do deposito
        '''
        # validacao 01: o deposito precisa ser maior que 0
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso.')
        else:
            print('Erro ao efetuar o deposit. Tente novamente.')


    def sacar(self: object, valor: float) -> None:
        '''
        Funcao que recebe um valor de saque. Caso o valor esteja dentro do saldo total disponivel,
        verifica se esta dentro do saldo da conta e atualiza os valores de saldo e saldo total
        disponivel. Caso negativo, zera o saldo e recalcula o limite, debitando o valor restante
        para completar a operacao de saque.

        Caso o valor esteja acima do saldo total disponivel, a operacao nao sera realizada.

        :params valor: o valor do saque.
        '''
        # validacao 01: o saque precisa ser maior que 0 e estar dentro do saldo disponivel (saldo + limite)
        if valor > 0 & self.saldo_total >= valor:
            # validacao 02: caso o valor do saque esteja dentro do saldo disponivel
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
            # validacao 03: caso o valor do saque esteja fora do saldo disponivel debitar o limite
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print('Saque efetuado com sucesso!')
        else:
            print('Saque não realizado. Tente novamente.')


    def transferir(self: object, destino: object, valor: float) -> None:
        '''
        Funcao que recebe um valor de transferencia. Caso o valor esteja dentro do saldo total disponivel
        da conta de origem (saldo + limite), verifica se esta dentro do saldo da conta de origem e atualiza 
        os valores de saldo e saldo total disponivel das contas de origem e destino. Caso negativo, zera o 
        saldo da conta e recalcula o limite da conta de origem, debitando o valor restante para completar a 
        operacao de transferencia e atualiza o saldo e saldo total disponivel da conta de destino.

        Caso o valor esteja acima do saldo total disponivel, a operacao nao sera realizada.

        :params valor: o valor da transferencia.
        :params destino: a conta de destino da transferencia.
        '''
        # validacao 01: o valor da conta de origem precisa ser maior que 0 e estar dentro 
        # do saldo disponivel na conta de origem (saldo + limite)
        if valor > 0 & self.saldo_total >= valor:
            # validacao 02: caso o valor do saque esteja dentro do saldo disponivel na conta de origem
            if self.saldo >= valor:
                # debitando a conta de origem
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total

                # creditando a conta de destino
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            # validacao 03: caso o valor do saque esteja fora do saldo disponivel na conta de origem
            # debitar o limite da conta de origem
            else:
                # debitando a conta de origem
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total

                # creditando a conta de destino
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            print('Tranferência efetuada com sucesso!')
        else:
            print('Transferência não realizada. Tente novamente.')
