from setup_finforecast import initialize_environment
import yfinance as yf

initialize_environment()

def download_data(tickers, start_date, end_date):
    """
    Downloads stock data from Yahoo Finance
    """
    data = yf.download(tickers, start=start_date, end=end_date)
    return data

# To test the function, let's download the last 5 years of data for Apple Inc. (ticker symbol AAPL)
data = download_data('AAPL', '2018-07-01', '2023-07-01')
print(data.head())