import requests

def obter_multiplas_cotacoes(pares):
    url = f"https://economia.awesomeapi.com.br/json/last/{'-'.join(pares)}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        for par in pares:
            chave = par.replace("-", "")
            if chave in dados:
                nome = dados[chave]['name']
                bid = dados[chave]['bid']
                print(f"💱 {nome} = {bid}")
            else:
                print(f"❌ Par {par} não encontrado.")
    else:
        print("Erro ao acessar a API.")

# Lista de pares que você quer consultar
pares = ['USD-AOA', 'USD-BRL', 'EUR-AOA', 'BRL-AOA', 'BTC-BRL']

# Executa
obter_multiplas_cotacoes(pares)
