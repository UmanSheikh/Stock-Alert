
# Stock Price Notifier using Twilio SMS

This script fetches the latest stock prices from Yahoo Finance and sends the information via SMS using Twilio. You can customize the stocks to monitor and receive real-time stock updates on your phone.

## Features

- Fetches stock prices from Yahoo Finance using `pandas_datareader`.
- Sends SMS notifications through Twilio.
- Easily customizable stock symbols and phone numbers.

## Requirements

- Python 3.7+
- A Twilio account (for sending SMS)
- Twilio credentials (account SID, auth token, Twilio number)
- Internet connection

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

2. Navigate to the project directory:

```bash
cd your-repo-name
```

3. Install the required Python packages:

```bash
pip install pandas_datareader twilio
```

## Configuration

1. Sign up for a [Twilio account](https://www.twilio.com/) and get your Account SID, Auth Token, and Twilio phone number.
2. Edit the `send_sms` function in the script and replace the following with your credentials:
    - `account_sid = "Your ID From Twilio"`
    - `auth_token = "Auth Token From Twilio"`
    - `sending = 'Twilio Number'`
    - `reciving = 'Your Recinving Number'`

## Usage

1. Run the script:

```bash
python script.py
```

The script will fetch stock prices of the listed companies and send them via SMS.

## Customization

- You can change the stock symbols to monitor by editing the `stocks` list in the `main()` function:

```python
stocks = ["AAPL", "JPM", "GOOGL", "SBUX"]
```

Simply add or remove stock symbols as per your needs.


