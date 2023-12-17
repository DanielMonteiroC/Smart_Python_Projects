# Vamos jogar aquele jokenpô, pedra - papel - tesoura ou o nome que for contra o computador?

import random  # Importa o módulo random para gerar escolhas aleatórias.
import time  # Importa o módulo time para introduzir atrasos.

def play():
    while True:  # Inicia um loop (While) infinito para o jogo até ser interrompido.
        choices = {'0': 'pedra', '5': 'papel', '2': 'tesoura'}  # Cria um dicionário ({}) para mapear a entrada do usuário para escolhas legíveis.

        user = input("'0' para pedra, '5' para papel, '2' para tesoura\nESCOLHA O SEU DESTINO: ")  # Solicita a entrada (input) do usuário.

        print("JAN\n...\n")  # \n é um comando de quebra de linha.
        time.sleep(1)  # Introduz um atraso de 1 segundo para efeito dramático usando o import time.
        print("KEN\n...\n")  
        time.sleep(1)  
        print("PON!!!\n")  

        computer = random.choice(list(choices.keys()))  # Escolhe aleatoriamente (random) uma chave (keys) do dicionário (choices) como a escolha do computador.

        if user == computer:  # Verifica se a escolha do usuário coincide com a escolha do computador.
            print("AIKO DESHOU!!!\n")  # Se sim (==), é um empate; imprime "AIKO DESHOU!!!".
        else:
            if is_win(user, computer, choices):  # Se não for um empate, verifica se o usuário vence usando a função is_win.
                print('Você Ganhou!')
            else:
                print('Sou um computador, o que esperava? Sua derrota é certa!')
            break  # Sai do loop.

def is_win(player, opponent, choices):
    win_conditions = [('0', '2'), ('2', '5'), ('5', '0')]  # Define as condições de vitória como tuplas (()) que são imutáveis.

    if (player, opponent) in win_conditions:  # Verifica se a tupla (player, opponent) está nas condições de vitória (True).
        return True
    else:
        print(f"Sabia que escolheria {choices[player]}.")  # Se não (False), imprime uma mensagem com a escolha do computador.
        return False

play()  # Chama a função (def) play no início do código para iniciar o jogo.