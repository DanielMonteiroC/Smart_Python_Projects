# Importa dois módulos necessários: 'random' para gerar números aleatórios e 'time' para medir o tempo de execução.
import random
import time

# Função de busca linear: percorre a lista e procura pelo elemento alvo.
def linear_search(lst, target):
    for i, value in enumerate(lst):
        # Verifica se o valor atual é igual ao alvo.
        if value == target:
            # Retorna o índice se encontrado.
            return i
    # Retorna -1 se o alvo não estiver na lista.
    return -1

# Função de busca binária: divide a lista pela metade repetidamente até encontrar o alvo.
def binary_search(lst, target, low=None, high=None):
    # Configura os valores padrão para low e high, se não forem fornecidos.
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1
    # Se a faixa de índices for inválida, retorna -1.
    elif high < low:
        return -1

    # Loop principal da busca binária.
    while low <= high:
        midpoint = (low + high) // 2

        # Verifica se o elemento do meio é o alvo.
        if lst[midpoint] == target:
            # Retorna o índice se encontrado.
            return midpoint
        # Atualiza os limites para continuar a busca.
        elif target < lst[midpoint]:
            high = midpoint - 1
        else:
            low = midpoint + 1
    # Retorna -1 se o alvo não for encontrado.
    return -1

# Parte principal do código
if __name__ == '__main__':
    # Configuração: gera uma lista ordenada de 10000 números aleatórios.
    length = 10000
    sorted_list = sorted(random.sample(range(-3 * length, 3 * length), length))
    
    # Medição do tempo da busca linear.
    start_time = time.time()
    for target in sorted_list:
        linear_search(sorted_list, target)
    end_time = time.time()
    linear_duration = end_time - start_time
    print(f"Pesquisa Linear: {linear_duration:.6f} segundos.")

    # Medição do tempo da busca binária.
    start_time = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end_time = time.time()
    binary_duration = end_time - start_time
    print(f"Pesquisa Binária: {binary_duration:.6f} segundos.")