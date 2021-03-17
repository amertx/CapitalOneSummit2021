from flask import Flask, render_template, url_for, request
import os
import requests
import json

app = Flask(__name__)


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

@app.route('/', methods=['GET','POST'])
def formInput():
    if request.method == 'POST':
        departure = request.form.get('departure')
        arrival = request.form.get('arrival')
        market = request.form.get('market')
        departureDestination = request.form.get('departureDestination')
        arrivalDestination = request.form.get('arrivalDestination')
        currency = request.form.get('currency')

        url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/"+market+"/"+ currency+"/en-US/"+ departureDestination+"-sky"+"/"+ arrivalDestination+"-sky"+"/" + departure+"/"+ arrival+""



        headers = {
            'x-rapidapi-key': "6bcc904facmshf03178edfc4450ap1e5c79jsn2d895f1c6d49",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        output = response.text

        return render_template('result.html', departure=departure, arrival=arrival,market=market, departureDestination=departureDestination, arrivalDestination=arrivalDestination, currency=currency, output=output)

@app.route("/airportSelections", methods=['GET', 'POST'])
def airportSelections():
    if request.method == 'POST':
        queryDestination = request.form.get('queryDestination')
        countryAirport = request.form.get('countryAirport')
        currencyAirport = request.form.get('currencyAirport')

        url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/"+countryAirport+"/"+currencyAirport+"/en-US/"

        querystring = {"query":queryDestination}

        headers = {
            'x-rapidapi-key': "6bcc904facmshf03178edfc4450ap1e5c79jsn2d895f1c6d49",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        outputAirport = response.json()


        return render_template('airports.html', queryDestination=queryDestination, countryAirport=countryAirport, currencyAirport=currencyAirport, outputAirport=outputAirport)
#input parameters

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
