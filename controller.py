from conta import Conta

# Função que criada para "escrever" os atributos do objeto pessoa no arquivo txt
def create(conta):
    
    # Manipulação do arquivo TXT
    contas = open('contas.txt', 'a')    # Abre 
    contas.write(f'{conta}\n')          # Escreve
    contas.close()                      # Fecha
    
    
# Função read
def read():
    
    lista_contas = list()               # Criação de uma lista vazia
    contas = open('contas.txt', 'r')    # Abre o arquivo TXT
    
    # Loop para manipulação do arquivo TXT
    # conta será cada linha contida em nosso arquivo TXT (contas)
    for conta in contas:
        
        # Criação de um objeto (lista) a partir de conta
        # Essa objeto foi "fracionado" em cada ";", removendo o ";"
        conta_objeto = conta.strip().split(';')    # Remoção dos espaços do inicio e fim da "linha"
        
        
        # Print solicitado no arquivo main.py
        print(conta_objeto)
        
        # Objeto de Conta
        conta = Conta()     # ['marcos', '798', '200.0']
        
        # Atribuindo valores no objeto através dos atributos do mesmo
        # Cada valor desse atributo será uma posição especifica de conta
        conta.titular = conta_objeto[0] # titular
        conta.numero = conta_objeto[1] # numero
        conta.saldo = conta_objeto[2] # saldo
        
        # Adicionando conta a lista lista_contas 
        lista_contas.append(conta)
    
    contas.close()          # Fecha o arquivo TXT
    return lista_contas     # Retorna lista_contas com o arquivo TXT nela (cada linha de TXT será um indice)


# Função update
def update(conta_update: Conta):        # Conta_update está referenciando a Classe Conta.
    
    lista_contas = list()               # Criação de uma lista vazia
    
    # Variável contas está recebendo o arquivo TXT
    contas = open('contas.txt', 'r')    # 'r' significa read / ler
    
    
    # Loop para manipulação do arquivo TXT
    # conta será cada linha do nosso arquivo TXT (contas)
    for conta in contas:
        
        # Criação de um objeto (lista) a partir de conta
        # Essa objeto foi "fracionado" em cada ";", removendo o ";"
        conta_objeto = conta.strip().split(';')    # Remoção dos espaços do inicio e fim da "linha"
        
        # Se conta_objeto na posição 1 (será numero da conta) for igual a 
        # conta_update.numero (informado pelo usuário no nosso arquivo main)
        if conta_update.numero == int(conta_objeto[1]):     # conta_update é nosso objeto da classe Conta
            
            # Irá adicionar o objeto (conta_update) na lista, para ser incerino no TXT posteriormente
            lista_contas.append(str(conta_update) + '\n')
            
        else:
            # Adicionando a string conta (cada linha do TXT) na lista, para ser incerino no TXT posteriormente
            lista_contas.append(conta)
    contas.close()      # Fecha read

    # Constas está recebendo o arquivo TXT 
    contas = open('contas.txt', 'w')    # 'w' significa write / escrever
    contas.writelines(lista_contas)     # Insere a lista com os objetos no arquivo TXT
    contas.close()                      # Fecha write
 

# Função delete
def delete(numero_conta):       # conta_update está referenciando a Classe Conta.
    
    lista_contas = list()               # Criação de uma lista vazia
        
    contas = open('contas.txt', 'r')    # contas está recebendo o arquivo TXT
    
    
    # Loop para manipulação do arquivo TXT
    # conta será cada linha do nosso arquivo TXT (contas)
    for conta in contas:
        # Criação de um objeto (lista) a partir de conta
        # Essa objeto foi "fracionado" em cada ";", removendo o ";"
        conta_objeto = conta.strip().split(';')    # Remoção dos espaços do inicio e fim da "linha"

        
        # Se numero_conta (numero de conta informado pelo usuário) 
        # For diferente de conta_objeto na posição 1 (int)
        # conta_objeto[1] (número da conta do nosso objeto que foi extraida do arquivo TXT)
        if numero_conta != int(conta_objeto[1]):
            
            # Esse if irá reescrever todos as linhas em nosso TXT, exeto a linha 
            # na qual o número da conta será o mesmo que o usuário deseja excluir
            
            lista_contas.append(conta)  # Colocando a variável conta do nosso "for" dentro da lista criana no inicio da função
            
        
    contas.close()  # Fecha read
        
    # Constas está recebendo o arquivo TXT 
    contas = open('contas.txt', 'w')    # 'w' significa write / escrever
    contas.writelines(lista_contas)     # Insere a lista com os objetos no arquivo TXT
    contas.close()  # Fecha write
