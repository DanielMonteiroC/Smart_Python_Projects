# Hashtags(#) são utilizadas para comentar uma linha de codigo. Aspas triplas(""") são usadas para comentar multiplas 
# linhas de codigo ou criar prints de multiplas linhas, deve ser aberto(""") e fechado(""").

# Importa o módulo 'time' para lidar com operações relacionadas ao tempo.
import time

"""
Define um nome de usuário (constante USERNAME) e senha (constante PASSWORD) fixos e atribui (=) o valor admin a ambos. 
É Uma boa prática utilizar nome maiúsculo para identificar constantes em Python.
""" 
USERNAME = 'admin'
PASSWORD = 'admin'

# Solicita ao usuário (input) para inserir um nome de usuário.
username_input = input('Usuário: ')

# Solicita ao usuário (input) para inserir uma senha.
password_input = input('Senha: ')

# Verifica se o nome de usuário e a senha inseridos são iguais (==) aos valores fixos (constantes USERNAME e PASSWORD).
if username_input == USERNAME and password_input == PASSWORD:
    # Se ambos correspondem, concede acesso utilizando o print que exibe o resultado na tela.
    print('Acesso Permitido!')
    print('Por favor, aguarde')

    """ 
    Simula um processo de carregamento com atrasos usando time.sleep (importado no inicio do codigo), 
    o f é chamado f-string e é usado para formatar a saida do codigo.
    """
    time.sleep(3)
    print('Ok... Loading...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Identidade confirmada!')
    print(f'Bem vindo a Matrix {USERNAME}')

# Se o nome de usuário corresponde (==), mas a senha não(!=):
elif username_input == USERNAME and password_input != PASSWORD:
    print('Senha Incorreta!')

# Se a senha corresponde(==), mas o nome de usuário não(!=):
elif username_input != USERNAME and password_input == PASSWORD:
    print('Usuário Incorreto!')

# Se nem o nome de usuário nem a senha correspondem (!=):
else:
    print('Entre em contato com algum agente!')