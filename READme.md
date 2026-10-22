# 📍 Buscador de CEP

Programa em Python que consulta um CEP na API pública [ViaCEP](https://viacep.com.br) e mostra o endereço correspondente no terminal.

Projeto criado para praticar o consumo de APIs REST, a leitura de respostas em JSON e a validação de dados de entrada.

## Funcionalidades

- Consulta de endereço a partir de um CEP (com ou sem traço)
- Validação do formato antes de chamar a API (8 dígitos numéricos)
- Aviso quando o CEP tem formato válido, mas não existe
- Exibição organizada de CEP, logradouro, bairro, cidade e estado

## Tecnologias

- Python 3
- Biblioteca [`requests`](https://pypi.org/project/requests/)
- API [ViaCEP](https://viacep.com.br)

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/Ryan-Oliveira-678/NOME-DO-REPOSITORIO.git
   cd NOME-DO-REPOSITORIO
   ```

2. Instale a dependência:

   ```bash
   python -m pip install requests
   ```

3. Rode o programa:

   ```bash
   python cep.py
   ```

## Exemplo de uso

```
Digite o seu CEP: 01001-000
=========================================
 CEP: 01001-000
 Logradouro: Praça da Sé
 Bairro: Sé
 Cidade: São Paulo
 Estado: SP
=========================================
```

Casos tratados:

| Entrada | Resultado |
|---|---|
| `01001000` ou `01001-000` | Mostra o endereço |
| `00000000` | "CEP não encontrado" |
| `abc` ou `123` | "Formato inválido" (a API nem é chamada) |

## Como funciona

1. O programa lê o CEP digitado e remove o traço
2. Valida se tem 8 caracteres e se são todos números
3. Faz uma requisição `GET` para `https://viacep.com.br/ws/{cep}/json/`
4. Converte a resposta JSON em dicionário Python
5. Se a resposta contém a chave `erro`, o CEP não existe; caso contrário, exibe os dados

## Próximos passos

- [ ] Tratar falhas de conexão com `try/except` e `timeout`
- [ ] Permitir várias consultas seguidas sem reiniciar o programa
- [ ] Buscar endereço por cidade e rua

## Autor

**Ryan** — estudante de Análise e Desenvolvimento de Sistemas

- GitHub: [Ryan-Oliveira-678](https://github.com/Ryan-Oliveira-678)
- LinkedIn: [Ryan Oliveira](https://linkedin.com/in/ryan-oliveira-952b2b38a)
