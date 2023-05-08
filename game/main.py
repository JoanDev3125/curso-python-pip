import random


# A la misma variable reemplazo el texto pero convertido en minúscula


def elegir_opcion():
    user_1 = input("Piedra, papel o tijera => ")
    options = ("piedra", "papel", "tijera")

    user_1 = user_1.lower()
    computer_option = random.choice(options)

    if not (user_1 in options):
        print("Elemento inválido para el juego")
        return None, None
    return user_1, computer_option


def reglas_juego(user_1, computer_option, user_wins, computer_wins):

    if (user_1 == computer_option):
        print("Ambos eligieron la misma opción")
    elif (user_1 == 'piedra'):
        if computer_option == 'tijera':
            print("Gana el usuario")
            user_wins += 1
        else:
            print("Gana la computadora")
            computer_wins += 1
    elif (user_1 == 'papel'):
        if computer_option == 'tijera':
            print("Gana la computadora")
            computer_wins += 1
        else:
            print("Gana el usuario")
            user_wins += 1
    elif (user_1 == 'tijera'):
        if computer_option == 'papel':
            print("Gana el usuario")
            user_wins += 1
        else:
            print("Gana el computador")
            computer_wins += 1

    return user_wins, computer_wins


def valida_ganador(user_wins, computer_wins):
    if computer_wins == 2:
        print("El ganador es la computadora")
        exit()
    if user_wins == 2:
        print("El ganador es el usuario")
        exit()


def ejecutar_juego():
    computer_wins = 0
    user_wins = 0
    round = 1
    while True:
        print(
            f"""*******************
            ROUND {round}
        *******************""")
        user_1, computer_option = elegir_opcion()
        user_wins, computer_wins = reglas_juego(
            user_1, computer_option, user_wins, computer_wins)

        round += 1
        valida_ganador(user_wins, computer_wins)


ejecutar_juego()
