import random

def gerar_cartoes(estatisticas, quantidade=10):
    mais_frequentes = [dezena for dezena, _ in estatisticas["mais_frequentes"]]
    todas_dezenas = list(range(100))

    cartoes = []
    for _ in range(quantidade):
        base = random.sample(mais_frequentes, k=min(10, len(mais_frequentes)))
        restante = list(set(todas_dezenas) - set(base))
        complemento = random.sample(restante, 10)
        cartao = sorted(base + complemento)
        cartoes.append(cartao)
    return cartoes
