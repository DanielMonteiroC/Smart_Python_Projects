# Define uma função (def) chamada pesquisa_binaria que realiza a busca binária para encontrar um número em um intervalo de 1 a 100.
def pesquisa_binaria(numero):
    # Inicializa as variáveis de início, fim e tentativas.
    inicio = 1
    fim = 100
    tentativas = 0

    # Enquanto o intervalo de busca não estiver vazio, continua o processo de busca.
    while inicio <= fim:
        # Calcula o ponto médio do intervalo.
        meio = (inicio + fim) // 2
        # Incrementa o contador de tentativas.
        tentativas += 1

        # Verifica se o número desejado foi encontrado.
        if meio == numero:
            # Retorna o número encontrado e o número de tentativas feitas.
            return meio, tentativas
        # Se o número estiver à direita do meio, ajusta o intervalo para a metade direita.
        elif meio < numero:
            inicio = meio + 1
        # Se o número estiver à esquerda do meio, ajusta o intervalo para a metade esquerda.
        else:
            fim = meio - 1

    # Retorna -1 para indicar que o número não foi encontrado, juntamente com o número de tentativas.
    return -1, tentativas

# Solicita ao usuário (input) que escolha um número (int) de 1 a 100.
numero_desejado = int(input("Escolha um número de 1 a 100:\n "))
# Chama a função (def) pesquisa_binaria para encontrar o número escolhido.
numero_encontrado, num_tentativas = pesquisa_binaria(numero_desejado)

# Exibe (print) o resultado com base na saída da função de pesquisa binária.
if numero_encontrado != -1:
    # Exibe uma mensagem indicando que o número foi encontrado, juntamente com o número de tentativas.
    print(f"O número {numero_encontrado} foi encontrado em {num_tentativas} tentativas!")
else:
    # Exibe uma mensagem indicando que o número não foi encontrado.
    print("O número não foi encontrado.")