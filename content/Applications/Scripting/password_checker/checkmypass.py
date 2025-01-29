import requests
import hashlib
import json
import sys


def test_didatico():
    # API exige que usemos um hash SHA1 para que n enviemos o password em si para o sistema que irá avaliar
    password = 'password123'
    hashed_password = 'cbfdac6008f9cab4083784cbd1874f76618d2a97'
    # vamos avaliar qualquer senha que começe com os 5 primeiro caracteres do nosso password com hash. Assim a api nunca vai saber nossa senha nem o hash dela
    url = 'https://api.pwnedpasswords.com/range/'+hashed_password[:5]
    res = requests.get(url)
    print(res)
    print(res.content)
    print(len(res.content))
    # sistemas de hashing são idempotente -> dado um input, sempre devolve o mesmo output


class checker:
    def __init__(self):
        pass

    def main(self, args):
        for password in args:
            password_hashed = self._hashing_password(password)
            api_response = self._request_api_data(password_hashed[:5])
            self._pwned_api_check(api_response, password_hashed, password)
        return 'Done!'

    def _hashing_password(self, password):
        return hashlib.sha1(password.encode('utf-8')).hexdigest()

    def _request_api_data(self, query_char):
        '''
        Entregamos os primeiros 5 caracteres da nossa senha e ele retorna os demais caracteres de passwords vazados
        '''
        url = 'https://api.pwnedpasswords.com/range/'+query_char
        res = requests.get(url)

        if res.status_code != 200:
            raise RuntimeError(
                f'Error fetching: {res.status_code} - {res.content}, verifique a api e teste novamente')
        return res

    def _pwned_api_check(self, api_response, password_hash, password):
        '''
        Checa se existe password na resposta da api
        '''
        def __read_responses(res):
            print(res.text)

        api_response_list_of_tails = {line.split(':')[0].upper(): line.split(':')[1]
                                      for line in api_response.text.splitlines()}

        password_tail = password_hash.upper()[5:]

        if password_tail in list(api_response_list_of_tails.keys()):
            print(
                f'Password {password} esta comprometido e aparece {api_response_list_of_tails[password_tail]} vezes no retorno da api pwned')
        else:
            print('Não existem evidencias de vazamento')
        pass


if __name__ == '__main__':
    CHECK = checker()
    sys.exit(CHECK.main(sys.argv[1:]))
