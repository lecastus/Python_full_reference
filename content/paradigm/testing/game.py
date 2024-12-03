import random
import sys


def comparar_numeros(numero_gerado, numero_chutado):
    try:
        if 0 < int(numero_chutado) <= 10:
            # checa se acertou
            if int(numero_chutado) == int(numero_gerado):
                return True, 'Parabens! Voce acertou!'

            else:
                return False, f'Não foi esse. O numero correto era {numero_gerado}'
        else:
            return False, 'Informe um numemo entre 1 e 10'
    except ValueError:
        return False, 'Por favor, informe um numero entre 1 e 10'


def recebe_um_numero():
    return input('Adivinhe o numero ')


def sorteia_um_numero():
    # random_num = random.randint(int(sys.argv[1]), int(sys.argv[2]))
    random_num = random.randint(0, 10)
    print('sorteado foi:', random_num)
    return random_num


def main():
    try:
        while True:

            # generate a number 1-10
            # generated_num = random.randrange(1, 10)

            # input from user?
            generated_num = sorteia_um_numero()
            input_user = recebe_um_numero()

            # check input

            result = comparar_numeros(generated_num, input_user)
            print(result[1])
            if result[0]:
                break

    except KeyboardInterrupt:
        print('\n   Obrigado por jogar')
