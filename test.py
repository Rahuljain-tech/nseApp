from nsetools import Nse
nse = Nse()
stock_data = nse.get_quote('RELIANCE')
print(stock_data)