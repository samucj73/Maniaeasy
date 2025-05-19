import requests

def obter_ultimos_concursos(qtd=25):
    url_base = "https://loteriascaixa-api.herokuapp.com/api/lotomania/"
    concursos = []

    ultimo_concurso = obter_ultimo_numero_concurso()
    if not ultimo_concurso:
        print("❌ Não foi possível determinar o número do último concurso.")
        return []

    for numero in range(ultimo_concurso, ultimo_concurso - qtd, -1):
        try:
            response = requests.get(f"{url_base}{numero}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                dezenas = data.get("dezenas", [])
                if dezenas and len(dezenas) == 20:
                    # Converte para int (sem .zfill) e ordena
                    dezenas_formatadas = sorted([int(d) for d in dezenas])
                    concursos.append(dezenas_formatadas)
                else:
                    print(f"⚠️ Dados incompletos no concurso {numero}")
            else:
                print(f"[HTTP {response.status_code}] Erro ao acessar concurso {numero}")
        except requests.exceptions.RequestException as e:
            print(f"[Erro de conexão] Concurso {numero}: {e}")
        except Exception as e:
            print(f"[Erro geral] Concurso {numero}: {e}")
    
    return list(reversed(concursos))  # Retorna os concursos do mais antigo ao mais recente

def obter_ultimo_numero_concurso():
    try:
        response = requests.get("https://loteriascaixa-api.herokuapp.com/api/lotomania", timeout=10)
        if response.status_code == 200:
            data = response.json()
            concurso = data.get("concurso")
            if concurso:
                return int(concurso)
            else:
                print("⚠️ Campo 'concurso' não encontrado na resposta da API.")
        else:
            print(f"[HTTP {response.status_code}] Erro ao acessar API principal.")
    except requests.exceptions.RequestException as e:
        print(f"[Erro de conexão] ao obter último concurso: {e}")
    except Exception as e:
        print(f"[Erro geral] ao obter último concurso: {e}")
    return None
