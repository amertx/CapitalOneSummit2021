from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return render_template('homePage.html')

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
