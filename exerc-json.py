import json, sys

file_json = sys.argv[1]

def read_json_file(file_json):
    with open(file_json) as j:
        content = json.loads(j.read())
    return content


print(read_json_file(file_json)) 
