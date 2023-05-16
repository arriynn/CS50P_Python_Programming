import requests
import sys

if len(sys.argv)!=2:
    sys.exit("Give command line argument")

try:
    number_of_bitcoin= float(sys.argv[1])
except ValueError:
    sys.exit("Argument is not a number")

response= requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
try:
    price_data= response.json()
    bitcoin_price= float(price_data["bpi"]["USD"]["rate"].replace(",", ""))
except requests.RequestException:
    sys.exit("Unable to retrieve Bitcoin data")

total_price= number_of_bitcoin*bitcoin_price

print(f"The total price of {number_of_bitcoin: ,} Bitcoin(s) is ${total_price: ,}")