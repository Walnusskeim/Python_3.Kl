"""
Python Sniping Bot for Vicinity Clothing. Example product is the Akimbo Lows Black Phantom.
❤
Maximilian
20.11.2023
"""

# Imports
import time
import config
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from requests_html import HTMLSession, AsyncHTMLSession



base_url = "https://www.vicinityclo.de/products/akimbo-lows-black-phantom?variant=43836856107274"  # Akimbo Lows Black Phantom in size 43
driver = webdriver.Firefox()
driver.get(base_url)


atc_btn = driver.find_element(by='id', value='ProductSubmitButton-template--18044749644042__main')  # Find the "Add To Cart" button

atc_btn.click() # Click the "Add To Cart" button
time.sleep(3)

checkout_btn = driver.find_element(by='id', value='CartDrawer-Checkout')    # Find the "Check Out" button
checkout_btn.click()
time.sleep(5)


###FOR SHOPIFY CHECKOUT###
print("Inputting checkout information...")
email_input = driver.find_element(by='id', value='email')  # Find the email input field
email_input.send_keys(config.email)    # Enter the email

firstname_input = driver.find_element(by='id', value='TextField1')  # Find the first name input field
firstname_input.send_keys(config.firstname)    # Enter the first name

lastname_input = driver.find_element(by='id', value='TextField2')  # Find the last name input field
lastname_input.send_keys(config.lastname)    # Enter the last name

shippingaddress_input = driver.find_element(by='id', value='shipping-address1')  # Find the shipping address input field
shippingaddress_input.send_keys(config.shippingaddress)    # Enter the shipping address

postalcode_input = driver.find_element(by='id', value='TextField5')  # Find the postal code input field
postalcode_input.send_keys(config.postalcode)    # Enter the postal code

city_input = driver.find_element(by='id', value='TextField6')  # Find the city input field
city_input.send_keys(config.city)    # Enter the city

phone_input = driver.find_element(by='id', value='TextField7')  # Find the phone input field
phone_input.send_keys(config.phone)    # Enter the phone number

continuetoshipping_btn = driver.find_element(by='id', value='QT4by _1fragemf4 rqC98 hodFu _7QHNJ VDIfJ j6D1f janiy')    # Find the "Continue to shipping" button
continuetoshipping_btn.click() # Click the "Continue to shipping" button

continuetopayment_btn = driver.find_element(by='id', value='QT4by _1fragemf4 rqC98 hodFu _7QHNJ VDIfJ j6D1f janiy')   # Find the "Continue to payment" button
continuetopayment_btn.click() # Click the "Continue to payment" button

cardnumber_input = driver.find_element(by='id', value='number')  # Find the card number input field
cardnumber_input.send_keys(config.cardnumber)    # Enter the card number

cardholder_input = driver.find_element(by='id', value='name')  # Find the card holder input field
cardholder_input.send_keys(config.cardholder)    # Enter the card holder

expiry_input = driver.find_element(by='id', value='expiry')  # Find the expiry input field
expiry_input.send_keys(config.expiry)    # Enter the expiry

cvv_input = driver.find_element(by='id', value='verification_value')  # Find the cvv input field
cvv_input.send_keys(config.cvv)    # Enter the cvv

paynow_btn = driver.find_element(by='id', value='QT4by _1fragemf4 rqC98 hodFu _7QHNJ VDIfJ j6D1f janiy')    # Find the "Pay now" button
paynow_btn.click() # Click the "Pay now" button

print("Product successfully sniped :P")
