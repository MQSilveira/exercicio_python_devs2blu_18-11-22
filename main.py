from conta import Conta
from controller import update, delete, create, read



# Função inicial do programa. O nome "menu" foi solicitado pelo profesor
def menu():
    
    pessoa = Conta()            # Criando um objeto de Conta()
    
    # Atribuição de valores para o objeto
    pessoa.numero = int(input('Informe o número da conta: '))
    pessoa.titular = str(input('Informe o nome do titular: '))
    pessoa.saldo = float(input('Informe o saldo inicial: '))

    # Adiciona atributos do objeto pessoa para o arqiuivo txt 
    create(pessoa)
    
    # Atribuindo informações contidas no arquivo txt via função read()
    lista_contas = read()
    
    
    # Print descritivo dos itens contidos no arquivo txt 
    print('\nItens do TXT')
    for c in lista_contas:
        print(f'Titular: {c.titular} > Número: {c.numero} > Saldo: {c.saldo}')
    
    
    # No documento main realize os testes com as nossas funções update e delete
    # Menu de interação para as funções update e delete

    # Cabeçalho
    print('='*5, ' Escolha uma das opções ', '='*5)
        
    opc = int(input('[1] UPDATE \n[2] DELETE \n:> '))   # Inseçao de opção
        
    match opc:
        case 1:     # UPDATE
            
            # Criando um novo objeto de Conta()
            conta_update = Conta()
            
            # Atribuindo valores no objeto através dos atributos do mesmo
            conta_update.numero = int(input('Digite o número da conta que será alterada: '))
            conta_update.titular = str(input('Novo titular: '))
            conta_update.saldo = float(input('Novo saldo inicial: '))
            
            # Função updade
            update(conta_update)
            
        case 2:     # DELETE
            
            numero_conta = int(input('Digite o número da conta que deseja excluir: '))
            
            delete(numero_conta)
        case _:
            print('Opção inválida')
     
     
# Chamando a função menu para iniciar nosso programa
menu()

