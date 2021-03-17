import requests
import json

query = input("Enter place: ")
country = input("Enter country: ")
currency = input("Enter currency: ")

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/"+country+"/"+currency+"/en-US/"

querystring = {"query":query}

headers = {
    'x-rapidapi-key': "6bcc904facmshf03178edfc4450ap1e5c79jsn2d895f1c6d49",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
parsedResponse = response.json()

print()
placesCounter=0
for key in parsedResponse['Places']:
    placesCounter+=1
    print(key["PlaceName"])
    print(key["CountryName"])
    print(key["PlaceId"])
    print()



print(placesCounter, " total airports found based on your query")

print()
