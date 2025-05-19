import requests

def obter_ultimos_resultados_lotomania(quantidade=25):
    url_ultimo = 'https://loteriascaixa-api.herokuapp.com/api/lotomania/latest'
    try:
        resposta = requests.get(url_ultimo)
        resposta.raise_for_status()
        ultimo_concurso = resposta.json()['concurso']
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o último concurso: {e}")
        return []

    resultados = []
    for numero in range(ultimo_concurso, ultimo_concurso - quantidade, -1):
        url = f'https://loteriascaixa-api.herokuapp.com/api/lotomania/{numero}'
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            dados = resposta.json()
            resultados.append(dados)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter o concurso {numero}: {e}")
            continue

    return resultados

# Exemplo de uso:
# resultados = obter_ultimos_resultados_lotomania()
# for resultado in resultados:
#     print(f"Concurso {resultado['concurso']} - Data: {resultado['data']}")
#     print(f"Dezenas: {resultado['dezenas']}")
#     print("-" * 40)
