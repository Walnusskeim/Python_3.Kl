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

# Replace the company names with the ones you want to track.
# You can add more companies by adding more elements to the list.
companys = ["AAPL", "MSFT", "VLKAF"]

def write_stock_price_to_file():
    for c in companys:
        company = yf.Ticker(c)
        data = company.history(period="1d")

        # Get the current price
        current_price = data['Close'][0]

        # Round the price to 2 decimal places
        current_price = round(current_price, 2)

        # Write into the file
        with open('stock_price.txt', 'a') as f:
            f.write(f'{time.ctime()} {c}: {current_price}\n')
            f.write('-----------------------------------\n')


# Create the file if it not already exists when the program starts
if not os.path.exists('stock_price.txt'):
    open('stock_price.txt', 'w').close()

# Write the stock price to the file every 30 minutes
while True:
    write_stock_price_to_file()
    print("Stock price written to file.")
    time.sleep(1800)  # Sleep for 30 minutes
