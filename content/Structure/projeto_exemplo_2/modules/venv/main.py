# O arquivo __init__.py declara uma pasta como um package

# importando um modulo de um package
from shopping.more_shopping import shopping_shelf
# importando um modulo de um package com um apelido por simplicidade
import shopping.shopping_cart as cart
# importando funções de um modulo. aqui, ao importar max nos substituimos a função max padrão de python e por isso vai dar erro
from utility import multiply, divide, max
# É possivel importar todas as funções de um modulo, mas isso traz o perigo de se importar uma função desconhecida que pode prejudicar o codigo, como o 'max' do exemplo
from utility import *

# print(multiply(2, 3))
# print(divide(2, 3))

# Uma pasta com modulos é um package
item = 'apple'
cart = cart.buy(item)
# print(cart)
# print(shopping_shelf.browse(item))

# Nome desse arquivo vai ser main mesmo que o nome do arquivo nao seja
# print(__name__)  # --> __main__

# Se estivermos rodando o arquivo principal da aplicação
# - muito util para criar funções de teste, pois elas so vao rodar quando o arquivo for rodado diretamente mas
# não quando for importado como biblioteca
if __name__ == '__main__':
    print('Rodando arquivo principal')

    import random
    # print(random)
    # help(random)
    # print(dir(random))
    # Numero aleatorio entre 0 e 1
    # print(random.random())
    # numero entre
    # print(random.randrange(1, 10))
    # aleatorio entre elementos de uma lista
    # print((random.choice(['a', 'f', 'z'])))
    # shuffle
    my_list = [1, 2, 3]
    random.shuffle(my_list)
    # print(my_list)

    import sys
    # print(sys)
    # sys argv é util para aplicar uma variavel no ato de rodar um script. Sys.argv serão os argumentos passados
    print(sys.argv)
