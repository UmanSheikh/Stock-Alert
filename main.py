import pandas_datareader as web
import time
from twilio.rest import Client

def send_sms(message):
    account_sid = "Your ID From Twilio"
    auth_token = "Auth Token From Twilio"
    sending = 'Twilio Number'
    reciving = 'Your Recinving Number' #Add your information
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
    stocks = ["AAPL", "JPM", "GOOGL", "SBUX"]    #You can change stock
    for j in range(0,4):
        data = get_stock_data(stocks[j])
        send_sms("\n\nStock price of \n\n{} is {}\n\nSent by: S World Codes".format(stocks[j], data))
        
            
        

    

if __name__ == '__main__':
    main()
