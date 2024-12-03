import unittest
import game
import inspect


class test_script(unittest.TestCase):

    def setUp(self):
        # função padrão do unittest. Serve para realizar alguma operação antes de cada teste
        print('Començando testes de função:')

    def testa_comparacao_de_numeros1(self):
        '''
        Comentario da funcao testa_comparacao_de_numeros
        '''
        print(inspect.stack()[0][3])  # printa o nome da função
        test_param_1 = 10
        test_param_2 = 10
        print('''
        test_param_1 = 10
        test_param_2 = 10
        ''')
        result = game.comparar_numeros(test_param_1, test_param_2)
        print(result)
        self.assertTrue(result[0])

    def testa_comparacao_de_numeros2(self):
        '''
        Comentario da funcao testa_comparacao_de_numeros
        '''
        print(inspect.stack()[0][3])  # printa o nome da função
        test_param_1 = 10
        test_param_2 = 1
        print('''
        test_param_1 = 10
        test_param_2 = 1
        ''')
        result = game.comparar_numeros(test_param_1, test_param_2)
        print(result)
        self.assertFalse(result[0])

    def testa_comparacao_de_numeros3(self):
        '''
        Comentario da funcao testa_comparacao_de_numeros
        '''
        print(inspect.stack()[0][3])  # printa o nome da função
        test_param_1 = 10
        test_param_2 = 'a'
        print('''
        test_param_1 = 10
        test_param_2 = 'a'
        ''')
        result = game.comparar_numeros(test_param_1, test_param_2)
        print(result)
        self.assertFalse(result[0])

    def tearDown(self) -> None:
        # Limpa variaveis. Acontece no fim de todo teste
        print('Limpando variaveis e objetos')
        print('---------------')
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()
