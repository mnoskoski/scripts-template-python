#/usr/bin/env python3
import sys
import json
#dicionario é uma estrutura de dados que armazena pares de chave-valor, permitindo acesso rápido aos valores através das chaves.
#exemplo de dicionario:

#args
file_json = sys.argv[1]

#function
def read_json_file(file_json):
    with open(file_json) as j:
        content = json.loads(j.read())
    return content

data = read_json_file(file_json)
for id, r in data.items():
    nome = r.get("nome")
    profissao = r.get("profissao")
    cidade = None
    if "endereco" in r:
        cidade = r["endereco"].get("cidade")
    else:
        cidade = r.get("cidade")
    print(f"nome: {nome}, profissao: {profissao}, cidade: {cidade}")



