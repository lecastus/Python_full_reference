import unittest
import script
import inspect


class test_script(unittest.TestCase):

    def setUp(self):
        # função padrão do unittest. Serve para realizar alguma operação antes de cada teste
        print('Començando testes de função:')

    def test_do_stuff(self):
        '''
        Comentario da funcao test_do_stuff
        '''
        print(inspect.stack()[0][3])  # printa o nome da função
        test_param = 10
        result = script.soma_cinco(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        '''
        Comentario da funcao test_do_stuff2
        '''
        print(inspect.stack()[0][3])  # printa o nome da função
        test_param = 'asdasdsa'
        result = script.soma_cinco(test_param)
        # ambos funcionam igual
        self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        '''
        Comentario da funcao test_do_stuff3
        '''
        print(inspect.stack()[0][3])  # printa o nome da função
        test_param = None
        result = script.soma_cinco(test_param)
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff4(self):
        '''
        Comentario da funcao test_do_stuff4
        '''
        print(inspect.stack()[0][3])  # printa o nome da função
        test_param = ''
        result = script.soma_cinco(test_param)
        self.assertIsInstance(result, ValueError)

    def tearDown(self) -> None:
        # Limpa variaveis. Acontece no fim de todo teste
        print('Limpando variaveis e objetos')
        print('---------------')
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()


# comandos
# python3 -m script_test -v
