#Leitura de arquivos
#usamos a funcao open()

import sys

#json_file = sys.argv[1]
json_file = "files/people.json"

def read_file(file_path):
    try:
        with open(file_path) as file:
            data = file.read()
        if "João Silva" in data:
            var = ("João is in the list")

    except FileNotFoundError:
        var = ("File not found")
    except Exception as e:
        var = f"An error occurred: {e}"
    else:
        var = "File read successfully"
    finally:
        print("Execution completed")
    return var

print(read_file(json_file))

