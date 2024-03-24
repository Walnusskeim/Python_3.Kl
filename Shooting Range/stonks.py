'''
Script, that shows the stock price of a company in a txt file every 30 minutes.
Maximilian
24.03.2024
❤
'''


##################################################
#                    Imports                     #
##################################################

import yfinance as yf
import time
import os


##################################################
#                     Code                       #
##################################################

def write_stock_price_to_file():
    # Replace "AAPL" with the short name of the company you want to track
    company = yf.Ticker("AAPL")
    data = company.history(period="1d")

    # Get the current price
    current_price = data['Close'][0]

    # Round the price to 2 decimal places
    current_price = round(current_price, 2)

    # Write into the file
    with open('stock_price.txt', 'a') as f:
        f.write(f'{time.ctime()}: {current_price}\n')


# Create the file if it not already exists when the program starts
if not os.path.exists('stock_price.txt'):
    open('stock_price.txt', 'w').close()

# Write the stock price to the file every 30 minutes
while True:
    write_stock_price_to_file()
    time.sleep(1800)  # Sleep for 30 minutes
