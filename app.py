from flask import Flask, render_template, url_for
import os
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/currencies"

    headers = {
        'x-rapidapi-key': "6bcc904facmshf03178edfc4450ap1e5c79jsn2d895f1c6d49",
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    currencies = response.json()

    return render_template('homePage.html', currencies=currencies)


#input parameters

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
