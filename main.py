from flask import Flask, jsonify, request, render_template, send_file
import os
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
@app.route('/getToken')
def getTok():
	getToken = requests.session()
	t = getToken.get('https://anuarioeco.uo.edu.cu/index.php/aeco/login',headers={"User-Agent":"TechDev_WebClient v01"})
	token = BeautifulSoup(t.text,"html.parser").find('input',attrs={"name":"csrfToken"})["value"]
	return token


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
