from flask import Flask, Response, request, json
from app import rabobank_service

app = Flask(__name__)


@app.route("/")
def home_view():
    return "<h1>Hello World</h1>"


@app.route("/rabobank/fetchaccounts", methods=['POST'])
def fetch_rabobank_accounts():
    return rabobank_service.fetch_accounts();
