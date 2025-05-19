from collections import Counter

def analisar_concursos(concursos):
    if not concursos:
        return {
            "total_concursos": 0,
            "mais_frequentes": [],
            "menos_frequentes": [],
            "pares_med": 0,
            "ímpares_med": 0,
            "soma_media": 0,
            "porcentagem_aparicao": {}
        }

    todas_dezenas = [d for c in concursos for d in c]
    total_concursos = len(concursos)

    contagem = Counter(todas_dezenas)
    mais_frequentes = contagem.most_common(10)
    menos_frequentes = contagem.most_common()[-10:]

    pares_med = sum([sum(1 for d in c if d % 2 == 0) for c in concursos]) / total_concursos
    ímpares_med = sum([sum(1 for d in c if d % 2 != 0) for c in concursos]) / total_concursos
    soma_media = sum([sum(c) for c in concursos]) / total_concursos

    porcentagem_aparicao = {dezena: (contagem[dezena] / total_concursos) * 100 for dezena in range(100)}

    return {
        "total_concursos": total_concursos,
        "mais_frequentes": mais_frequentes,
        "menos_frequentes": menos_frequentes,
        "pares_med": pares_med,
        "ímpares_med": ímpares_med,
        "soma_media": soma_media,
        "porcentagem_aparicao": porcentagem_aparicao
    }
