from flask import json
from base64 import b64encode
from Crypto.Hash import SHA512
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

import requests


def fetch_accounts(request):
    data = request.form.to_dict()

def generate_rsa_signature(message, private_key_file):
    message = """date: Tue, 18 Sep 2018 09:51:01 GMT
    digest: sha-512=z4PhNX7vuL3xVChQ1m2AB9Yg5AULVxXcg/SpIdNs6c5H0NE8XYXysP+DGNKHfuwvY7kxvUdBeoGlODJ6+SfaPg==
    x-request-id: 95126d8f-ae9d-4ac3-ac9e-c357dcd78811"""

    digest = SHA512.new()
    digest.update(message.encode("utf-8"))
    private_key = False

    with open(private_key_file, "r") as myfile:
        private_key = RSA.importKey(myfile.read())

    signer = PKCS1_v1_5.new(private_key)
    signature = signer.sign(digest)
    return b64encode(signature)


def get_request_with_tls(request, resource):
    url = 'https://webservices-moneytun.staging.wwcny.com/' + resource
    params = request.args.to_dict()

    response = requests.get(url, params=params, headers=request.headers, cert=('cert.pem', 'key.pem'))
    return {'payload': response.text, 'status': response.status_code}
