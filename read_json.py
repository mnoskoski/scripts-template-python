import os
import json
import sys

jsonFile = sys.argv[1]

with open(jsonFile, 'r') as f:
    # Ler o conteúdo do arquivo JSON
    file2 = json.load(f)
    
    #print(f"Conteúdo do JSON:\n{file2}")
    
    cidades = [registro['cidade'] for registro in file2 if 'cidade' in registro]
    print(f"cidades do json :\n{ cidades }")