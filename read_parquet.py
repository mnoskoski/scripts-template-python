#import sys
#
#import pandas as pd
#parqueMaroto = pd.read_parquet('./parquet/prep1.parquet')
#print(parqueMaroto.head()) #exibe somente as 5 primeiras linhas


import pandas as pd
# Lendo o arquivo Parquet
parqueMaroto = pd.read_parquet('./parquet/prep1.parquet')
# Alterando a configuração para exibir todas as linhas
pd.set_option('display.max_rows', None)
# Exibindo o DataFrame completo
print(parqueMaroto)


## read excel using pandas

#import pandas as pd
#path= sys.argv[1]
#arquivo= sys.argv[2]
#
## Testar leitura sem filtros
#df = pd.read_excel(f'{path}/{arquivo}', sheet_name='PLANILHA1') #planilha1 - nome da aba no excel
#print(df.columns)