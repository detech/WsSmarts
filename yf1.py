from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import pandas as pd
from datetime import date

#Reference: https://medium.com/@jouneidraza522/yahoo-finance-api-to-get-stocks-tickers-data-in-python-c49820249a18
#https://www.youtube.com/watch?v=eSpH6fPd5Yw

# Stock tickers for which data will be fetched
#ticker_list=['DJIA', 'DOW', 'LB', 'EXPE', 'PXD', 'MCHP', 'CRM', 'JEC', 'NRG', 'HFC', 'NOW']
ticker_list=['DJIA', 'DOW']
today=date.today()
files=[]

#Specify historical price date range
start_date="2017-01-01"
end_date="2019-11-30"

#Method to get the ticker data and save to a file
def getData(ticker):
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    dataname=ticker+'_'+str(today)
    files.append(dataname)
    SaveData(data, dataname)

# Method to save the given pandas data to a csv file
def SaveData(df, filename):
    print('saving to ' + './data/'+filename+'.csv')
    # df.to_csv('./data/'+filename+'.csv')

def printDataSummary():
    for i in range(0,len(ticker_list)):
        print('reading from ' + './data/'+str(files[i])+'.csv')
        # df1=pd.read_csv('./data/'+str(files[i])+'.csv')
        # print(df1.head())

for tik in ticker_list:
    getData(tik)

printDataSummary()


    
                    

