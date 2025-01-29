# Adicionando '/robots.txt' no final de uma url -> mensagem com o que é possivel e o que não é com robos
import requests
from bs4 import BeautifulSoup

url = 'https://www.warhammer-community.com/en-gb/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')


def coleta_dados(dados):
    pg = []
    for idx, item in enumerate(dados):
        title = dados[idx].getText()
        href = dados[idx].get('href', None)s
        pg.append({'title': title, 'link': href})
    return pg


def coleta_dados_por_id(ids):
    pg = []
    for id in ids:
        dados = soup.find(id=id)
        if dados is not None:
            print(dados)
            return
            title = dados['title']
            link = dados['link']
            pg.append({'title': title, 'link': link})
    return pg


# dados = soup.find_all('a')
# print(coleta_dados(dados))


ids = soup.select('.hidden')
print(coleta_dados_por_id(ids))

# print(dados)
