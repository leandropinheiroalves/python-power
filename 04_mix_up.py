"""
04. mix_up

Dadas as strings a e b, retorne uma string com a e b separados
por um espaço '<a> <b>', além disso, troque os 2 primeiros caracteres
das duas strings.

Exemplo:
    'mix', 'pod' -> 'pox mid'
    'dog, 'dinner' -> 'dig donner'

Assuma que a e b tem tamanho 2 ou maior.
"""


def mix_up(a, b):
    # +++ SUA SOLUÇÃO +++
    # SOLUÇÃO 1
    # iniciais_palavra1 = a[:2]
    # resto_palavra1 = a[2:]
    # iniciais_palavra2 = b[:2]
    # resto_palavra2 = b[2:]
    # resultado = iniciais_palavra2 + resto_palavra1 + ' ' + iniciais_palavra1 + resto_palavra2
    # return resultado

    # SOLUÇÃO 2 REPLACE
    # palavra1 = a.replace(a[:2], b[:2])
    # palavra2 = b.replace(b[:2], a[:2])
    # return palavra1 + ' ' + palavra2

    # SOLUÇÃO EM UMA LINHA
    # return a.replace(a[:2], b[:2]) + ' ' + b.replace(b[:2], a[:2])

    # SOLUÇÂO EM UMA LINHA USANDO .JOIN
    return ' '.join((a.replace(a[:2], b[:2]), b.replace(b[:2], a[:2])))

    # ADICIONADO 2 TESTES COM PALAVRAS COM MENOS DE 3 LETRAS

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(mix_up, ('mix', 'pod'), 'pox mid')
    test(mix_up, ('dog', 'dinner'), 'dig donner')
    test(mix_up, ('gnash', 'sport'), 'spash gnort')
    test(mix_up, ('pezzy', 'firm'), 'fizzy perm')
    test(mix_up, ('ab', 'cd'), 'cd ab')
    test(mix_up, ('h', 's'), 's h')
