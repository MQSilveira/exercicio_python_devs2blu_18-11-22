
# Classe Conta
class Conta:
    
    # criando atributos de classe privados
    __titular = ''
    __numero = ''
    __saldo = ''
    
    
    # Criação se Getter e Setter para os atributos de Classe via Propriedade
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # Método String
    def __str__(self):
        return f'{self.titular};{self.numero};{self.saldo}'
