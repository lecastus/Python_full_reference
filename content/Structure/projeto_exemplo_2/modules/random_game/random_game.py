import random
import sys
generated_num = random.randint(int(sys.argv[1]), int(sys.argv[2]))
try:
    while True:

        # generate a number 1-10
        # generated_num = random.randrange(1, 10)

        # input from user?
        print('sorteado foi:', generated_num)
        input_user = input('Adivinhe o numero ')

        # check input
        try:
            if 0 < int(input_user) < 10:
                # checa se acertou
                if int(input_user) == int(generated_num):
                    print('Parabens! Voce acertou!')
                    break
                else:
                    print(
                        f'Não foi esse. O numero corretou era {generated_num}')
            else:
                print('Informe um numemo entre 1 e 10')
        except ValueError:
            print('Por favor, informe um numero entre 1 e 10')
            continue


except KeyboardInterrupt:
    print('\n   Obrigado por jogar')
