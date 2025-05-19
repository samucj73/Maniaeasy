import requests

def obter_ultimos_concursos(quantidade=25):
    """
    Coleta os últimos `quantidade` concursos da Lotomania.
    Retorna uma lista de listas com 20 dezenas sorteadas em cada concurso (como inteiros).
    """
    url_ultimo = 'https://loteriascaixa-api.herokuapp.com/api/lotomania/latest'
    try:
        resposta = requests.get(url_ultimo, timeout=10)
        resposta.raise_for_status()
        ultimo_concurso = resposta.json().get('concurso')
        if not ultimo_concurso:
            print("❌ Erro: campo 'concurso' não encontrado na resposta.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao obter o último concurso: {e}")
        return []

    resultados = []
    for numero in range(ultimo_concurso, ultimo_concurso - quantidade, -1):
        url = f'https://loteriascaixa-api.herokuapp.com/api/lotomania/{numero}'
        try:
            resposta = requests.get(url, timeout=10)
            resposta.raise_for_status()
            dados = resposta.json()
            dezenas = dados.get("dezenas", [])
            if dezenas and len(dezenas) == 20:
                dezenas_numeros = sorted([int(d) for d in dezenas])
                resultados.append(dezenas_numeros)
            else:
                print(f"⚠️ Concurso {numero} com dezenas inválidas: {dezenas}")
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Erro ao obter o concurso {numero}: {e}")
            continue

    return resultados
