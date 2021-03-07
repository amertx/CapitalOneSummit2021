import requests
import json
from collections import Counter

#country of origin
market = input("Enter market: ")

#input parameters
origin = input("Enter origin: ")
arrival = input("Enter arrival: ")

#departure & arrival dates
dateDeparture = input("Enter departure date (YYYY-MM-DD): ")
dateArrival = input("Enter arrival date (YYYY-MM-DD): ")

#Currency
currency = input("Enter currency: ")

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/"+market+"/"+ currency+"/en-US/"+ origin+"-sky"+"/"+ arrival+"-sky"+"/" + dateDeparture+"/"+ dateArrival+""



headers = {
    'x-rapidapi-key': "6bcc904facmshf03178edfc4450ap1e5c79jsn2d895f1c6d49",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
parsedResponse = response.json()

quoteCounter=0
for key in parsedResponse["Quotes"]:
    print(key["QuoteId"])

print(quoteCounter, " total quotes found")
