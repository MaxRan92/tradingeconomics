import requests
import tradingeconomics as te
import pandas as pd
import json

def get_data():
    te.login()
    indicators = te.getWBIndicator(series_code = 'fr.inr.rinr', output_type='df')
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):   more options can be specified also
    print(indicators)
    # URL ='https://api.tradingeconomics.com/country/Mexico?c=guest:guest&f=json'
    # df = pd.read_json(URL)
    # print(df)
    


get_data()