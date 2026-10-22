import requests

cep = input("Digite o seu CEP: ").replace("-", "").strip()

if len(cep) != 8 or not cep.isdigit():
    print("Formato invalido. O CEP deve conter 8 dígitos numéricos.")

else:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    dados = resposta.json()

    if "erro" in dados: 
        print("CEP não encontrado. Verifique se o CEP digitado está correto.")
    else:
        print(f'========================================= \n CEP: {dados["cep"]} \n Logradouro: {dados["logradouro"]} \n Bairro: {dados["bairro"]} \n Cidade: {dados["localidade"]} \n Estado: {dados["uf"]} \n =========================================')