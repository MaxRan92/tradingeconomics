import tradingeconomics as te

def get_data():
    te.login()
    indicators = te.getIndicatorData(country=['mexico', 'sweden'], output_type='df')
    print(indicators)

get_data()