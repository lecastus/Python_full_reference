import sys
import os
from pathlib import Path
from PIL import Image


def carrega_variaveis_de_entrada():
    '''recebe o primeiro e segundo argumento'''
    pasta_fonte = sys.argv[1]
    pasta_destino = sys.argv[2]
    return pasta_fonte, pasta_destino


def maneja_pastas_envolvidas(pasta_fonte, pasta_destino):
    '''checar se a pasta destino existe, se não existir, criamos'''
    try:
        print(pasta_fonte)
        os.listdir(pasta_fonte)
    except Exception as e:
        return False, f'pasta fonte não existe. {e}'

    try:
        os.listdir(pasta_destino)
    except Exception as e:
        return True, 'Pasta destino não existe. Uma nova foi criada com o nome pedido'

    return True, 'Pasta destino confirmada.'


def converte_imagens_da_pasta_fonte(pasta_fonte):
    '''Iterar por toda a pasta'''
    todos_os_arquivos_da_pasta_fonte = os.listdir(pasta_fonte)
    dict_arquivos = {}
    for arquivo in todos_os_arquivos_da_pasta_fonte:
        dict_arquivos[arquivo] = Image.open(pasta_fonte+'\\'+arquivo)
    return dict_arquivos


def salva_arquivos_convertidos(dict_arquivos, pasta_destino):
    # salvar na nova pasta, converter imagem por imagem
    for arquivo in dict_arquivos.keys:
        dict_arquivos[arquivo].save(
            pasta_destino+'\\'+arquivo.replace('jpg', 'png'))


def main():
    pasta_fonte, pasta_destino = carrega_variaveis_de_entrada()
    condicao, msg = maneja_pastas_envolvidas(pasta_fonte, pasta_destino)
    print(msg)
    if condicao is False:
        return
    dict_arquivos = converte_imagens_da_pasta_fonte(pasta_fonte)
    salva_arquivos_convertidos(dict_arquivos, pasta_destino)


main()
