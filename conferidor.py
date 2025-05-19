def conferir_cartoes(cartoes, concursos):
    resultados = []
    for cartao in cartoes:
        acertos_por_concurso = []
        for resultado in concursos:
            acertos = len(set(cartao).intersection(resultado))
            acertos_por_concurso.append(acertos)
        resultados.append(acertos_por_concurso)
    return resultados

def calcular_retorno(cartoes, concursos):
    tabela_premios = {
        20: 3000000,  # valor simbólico
        19: 20000,
        18: 500,
        17: 100,
        16: 20,
        15: 5,
        0: 100000
    }
    custo_total = len(cartoes) * 2.5
    retorno_total = 0

    resultados = conferir_cartoes(cartoes, concursos)
    for acertos_conc in resultados:
        for acertos in acertos_conc:
            retorno_total += tabela_premios.get(acertos, 0)

    return custo_total, retorno_total, retorno_total - custo_total
