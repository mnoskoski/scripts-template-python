import json
import sys

def replace_variables_in_json(file_path):
    # Abrir o arquivo JSON
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
#
    if "userID10" in data and "name" in data["userID10"]:
        print(data["userID10"]["name"])

    # Substituir a linha específica 'apiVersionSetId' usando as variáveis
    #api_version_set_id = f"userID1: {username}"

    ## Realizar o replace das variáveis
    #json_str = json_str.replace("$(azure_subscription)", azure_subscription)
    #json_str = json_str.replace("$(ApimResourceGroup)", ApimResourceGroup)
    #json_str = json_str.replace("$(apim_name)", apim_name)
#
    ## Converter a string de volta para JSON
    #updated_data = json.loads(json_str)
#
    ## Sobrescrever o arquivo JSON com as mudanças
    #with open(file_path, 'w') as json_file:
    #    json.dump(updated_data, json_file, indent=4)
#
    #print(f"Variáveis substituídas com sucesso no arquivo: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Uso: python script.py <caminho_arquivo_json>")
    else:
        file_path = sys.argv[1]
        #username = sys.argv[2]
        #ApimResourceGroup = sys.argv[3]
        #apim_name = sys.argv[4]
        replace_variables_in_json(file_path)