import requests

def obter_cotacao(moeda_base='USD', moeda_destino='AOA'):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_base}-{moeda_destino}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        par = moeda_base + moeda_destino
        valor = dados[par]['bid']
        print(f"💰 1 {moeda_base} = {valor} {moeda_destino}")
    else:
        print("Erro ao obter a cotação.")
pares = ['USD-AOA', 'USD-BRL', 'EUR-AOA', 'BRL-AOA', 'BTC-BRL']
# Exemplo de uso:
obter_cotacao()
