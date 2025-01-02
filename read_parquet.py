import sys

import pandas as pd
parqueMaroto = pd.read_parquet('./parquet/tb_region.parquet')
print(parqueMaroto.head())

## read excel using pandas

import pandas as pd
path= sys.argv[1]
arquivo= sys.argv[2]

# Testar leitura sem filtros
df = pd.read_excel(f'{path}/{arquivo}', sheet_name='PLANILHA1') #planilha1 - nome da aba no excel
print(df.columns)