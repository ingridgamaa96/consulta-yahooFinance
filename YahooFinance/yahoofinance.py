#Pegar cotações do Yahoo Finance Com Python 

import pandas as pd
import pandas_datareader.data as pdr 
import yfinance 


yfinance.pdr_override()

ativos = ["ITAUB3.SA", "VALE3.SA", "PETR3.SA" , "^BVSP" ] 

data_inicial = "2023-1-01"
data_final = "2023-08-30"



tabela_cotacoes = pdr.get_data_yahoo("^BVSP" , data_inicial , data_final)["Adj Close"]
print(tabela_cotacoes) 