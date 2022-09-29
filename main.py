import pandas_datareader as web
import time
from twilio.rest import Client

def send_sms(message):
    account_sid = "ACcf171db624b50b3aa5c0a81bd21338a2"
    auth_token = "28108efab2a7c5ae54057d01521ee3b1"
    sending = '+12283386202'
    reciving = '+923217727595'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=sending,
        to=reciving
    )

def get_stock_data(stock):
    data = web.DataReader(stock, data_source='yahoo').iloc[-1]['Close']
    return data

def main():
    stocks = ["AAPL", "JPM", "GOOGL", "SBUX"]    
    for j in range(0,4):
        data = get_stock_data(stocks[j])
        send_sms("\n\nStock price of \n\n{} is {}\n\nSent by: Uman Sheikh".format(stocks[j], data))
        
            
        

    

if __name__ == '__main__':
    main()
