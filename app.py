from flask import Flask, render_template, url_for, request
import os
import requests
import json

app = Flask(__name__)

#homepage routing
@app.route('/', methods=['GET'])
def base():
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/currencies"

    headers = {
        'x-rapidapi-key': "6bcc904facmshf03178edfc4450ap1e5c79jsn2d895f1c6d49",
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    currencies = response.json()

    return render_template('homePage.html', currencies=currencies)

#form validation
@app.route('/', methods=['GET','POST'])
def formInput():
    if request.method == 'POST':
        #extract inputs from html input tags
        departure = request.form.get('departure')
        arrival = request.form.get('arrival')
        departureDestination = request.form.get('departureDestination')
        arrivalDestination = request.form.get('arrivalDestination')
        currency = request.form.get('currency')

        url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsedates/v1.0/US/"+ currency+"/en-US/"+ departureDestination+"-sky"+"/"+ arrivalDestination+"-sky"+"/" + departure+"/"+ arrival+""

        headers = {
            'x-rapidapi-key': "6bcc904facmshf03178edfc4450ap1e5c79jsn2d895f1c6d49",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        parsedResponse = response.json()

        #variables for extracting quotes from GET request
        outputArray=[]
        quoteCounter=0
        carrierOutBound=""
        carrierInBound=""

        #dictionary for all airlines found
        carrier={'CarrierId':'Name'}

        for key in parsedResponse['Carriers']:
            carrier[key["CarrierId"]]= key["Name"]

        for key in parsedResponse['Quotes']:
            outputArray.append("Q  U  O  T  E: #"+str(key["QuoteId"]))
            outputArray.append("Price: $" + str(key["MinPrice"]))
            for key4 in parsedResponse['Currencies']:
                quoteCounter+=1


            carrierOutBound= key["OutboundLeg"]["CarrierIds"]

            for key2 in carrier:
                if carrierOutBound[0] == key2:
                    outputArray.append(carrier[key2])

            outputArray.append("Departure Date: " + str(key["OutboundLeg"]["DepartureDate"]))

            placeCounter=0
            for key5 in parsedResponse['Places']:
                if placeCounter == 0:
                    outputArray.append("         DEPARTURE INFORMATION")
                    outputArray.append("Departure Name: "+ str(key5["Name"]))
                    outputArray.append("Airport Code: " + str(key5["SkyscannerCode"]))
                    outputArray.append("City: " + str(key5["CityName"]))
                    outputArray.append("Country Name: "+ str(key5["CountryName"]))
                elif placeCounter == 1:
                    outputArray.append("         ARRIVAL INFORMATION")
                    carrierInBound= key["InboundLeg"]["CarrierIds"]
                    for key3 in carrier:
                        if carrierInBound[0] == key3:
                            outputArray.append("Airline: " + str(carrier[key3]))
                    outputArray.append("Arrival Date: " + str(key["InboundLeg"]["DepartureDate"]))
                    outputArray.append("Arrival Name: " + str(key5["Name"]))
                    outputArray.append("Airport Code: " + str(key5["SkyscannerCode"]))
                    outputArray.append("City: " + str(key5["CityName"]))
                    outputArray.append("Country: " +str(key5["CountryName"]))
                placeCounter+=1
            outputArray.append(" ")


        return render_template('result.html', departure=departure, arrival=arrival, departureDestination=departureDestination, arrivalDestination=arrivalDestination, currency=currency, parsedResponse=parsedResponse, outputArray=outputArray, quoteCounter=quoteCounter)

@app.route("/airportSelections", methods=['GET', 'POST'])
def airportSelections():
    if request.method == 'POST':
        #extraction for each input tag
        queryDestination = request.form.get('queryDestination')
        countryAirport = request.form.get('countryAirport')
        currencyAirport = request.form.get('currencyAirport')

        url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/"+countryAirport+"/"+currencyAirport+"/en-US/"

        querystring = {"query":queryDestination}

        headers = {
            'x-rapidapi-key': "6bcc904facmshf03178edfc4450ap1e5c79jsn2d895f1c6d49",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
            }

        #based on initial query by user, local airports will be found
        response = requests.request("GET", url, headers=headers, params=querystring)
        outputAirport = response.json()


        return render_template('airports.html', queryDestination=queryDestination, countryAirport=countryAirport, currencyAirport=currencyAirport, outputAirport=outputAirport)
#input parameters

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
