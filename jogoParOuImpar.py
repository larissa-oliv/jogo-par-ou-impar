import random  # Importa o módulo random para gerar números aleatórios

def par_ou_impar():
    vitorias = 0  # Inicializa o contador de vitórias do jogador
    derrotas = 0  # Inicializa o contador de derrotas do jogador

    print("Bem-vindo ao jogo de Par ou Ímpar!\n")

    while True:
        # Recebe a escolha do jogador: Par ou Ímpar
        escolha_jogador = input("Escolha Par ou Ímpar (P/I): ").strip().upper()
        while escolha_jogador not in ['P', 'I']:
            escolha_jogador = input("Escolha inválida. Por favor, escolha Par (P) ou Ímpar (I): ").strip().upper()

        # Recebe o intervalo de números que o jogador deseja usar
        intervalo = int(input("Escolha o intervalo máximo de números (exemplo: 10 para 1 a 10): "))

        # Recebe o número escolhido pelo jogador
        numero_jogador = int(input(f"Escolha um número de 1 a {intervalo}: "))

        # Gera um número aleatório para o computador
        numero_computador = random.randint(1, intervalo)
        print(f"O número do computador é: {numero_computador}")

        # Calcula a soma dos números
        soma = numero_jogador + numero_computador
        print(f"A soma dos números é: {soma}")

        # Verifica se a soma é Par ou Ímpar
        resultado = "P" if soma % 2 == 0 else "I"

        # Determina o vencedor
        if resultado == escolha_jogador:
            print("Parabéns! Você ganhou esta rodada!\n")
            vitorias += 1
        else:
            print("Você perdeu esta rodada. Tente novamente!\n")
            derrotas += 1

        # Exibe o placar
        print(f"Placar: {vitorias} Vitórias - {derrotas} Derrotas")

        # Pergunta se o jogador quer jogar novamente
        jogar_novamente = input("Quer jogar novamente? (S/N): ").strip().upper()
        if jogar_novamente != 'S':
            print("Obrigado por jogar! Até a próxima.")
            break

# Chama a função para iniciar o jogo
par_ou_impar()
