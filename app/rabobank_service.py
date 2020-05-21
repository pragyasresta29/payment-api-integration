from flask import json
from base64 import b64encode
from Crypto.Hash import SHA512
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

import requests


def fetch_accounts():
    resource = 'payments/account-information/ais/v3/accounts/'
    request = {}
    request.headers = {
        'accept': 'application/json',
        'authorization': 'Bearer "AAIkYjc0YjNlZDQtMTMxNC00MTMyLTkwMjQtODNlNzQwYjExYzM5k9Y-hbWfCxrQcfrWbwHYSBRPzI66-B0gXOQOs2T_NCnm0r9w1aJptTzJ3YBLZjtrCBjA81Uv1R5vcR7WyXV0wO_0RIcSbjWf8JMdJK3H2F0rDmOGRJ3dfe2G23zLcJvd_eZz6IX-Kc2YFmaz-_Foe2OBfVSYjUbGxfTo1brqtid_zp7qRetbkeHRdIFjZ2o8koYWWOFkgyp4H9ACTKgCbw',
        'date': 'Tue, 18 Sep 2018 09:51:01 GMT',
        'digest': 'sha-512=z4PhNX7vuL3xVChQ1m2AB9Yg5AULVxXcg/SpIdNs6c5H0NE8XYXysP+DGNKHfuwvY7kxvUdBeoGlODJ6+SfaPg==',
        'psu-ip=address': '127.0.0.1',
        'signature': 'keyId="1523433508",algorithm="rsa-sha512",headers="date digest x-request-id",signature="y5o7gKxmfA6AT6IvZ5L89uWxhjcw0BPqDlfK6WX1pB5vKtOctzwustjHI6TjdgQMzQL9LAJX6izs5lVCB6Bjl/l3ntCt4rigJPzfTLbnSlxBhLcabru+KyC7pu00NasyMzl4kv/1jtxrBqzSsUvCz87IBSTLSeoPCJc4E5ME82Bdpss67RWcVe94UzLW8jsCqrncLxiMsD6d2ZQmnH/S7Gu9zk8g9eJovmLIaVLn4C5vW7khS63hSZf8qdTEDlMI/L+QgYVgZVIijKosYEnCB9tH5OYWS9cQ1g1NBrMHQASg/ZV8CxHkXizYg7gQoTGaKvSeD7QC172OqySblE1A9Q==',
        'tpp-signature-certificate': 'MIIDkDCCAnigAwIBAgIEWs3AJDANBgkqhkiG9w0BAQsFADCBiTELMAkGA1UEBhMCTkwxEDAOBgNVBAgMB1V0cmVjaHQxEDAOBgNVBAcMB1V0cmVjaHQxETAPBgNVBAoMCFJhYm9iYW5rMRwwGgYDVQQLDBNPbmxpbmUgVHJhbnNhY3Rpb25zMSUwIwYDVQQDDBxQU0QyIEFQSSBQSSBTZXJ2aWNlcyBTYW5kYm94MB4XDTE4MDQxMTA3NTgyOFoXDTIzMDQxMTA3NTgyOFowgYkxCzAJBgNVBAYTAk5MMRAwDgYDVQQIDAdVdHJlY2h0MRAwDgYDVQQHDAdVdHJlY2h0MREwDwYDVQQKDAhSYWJvYmFuazEcMBoGA1UECwwTT25saW5lIFRyYW5zYWN0aW9uczElMCMGA1UEAwwcUFNEMiBBUEkgUEkgU2VydmljZXMgU2FuZGJveDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANoAjqGWUgCIm2F+0sBSEwLal+T3u+uldLikpxHCB8iL1GD7FrRjcA+MVsxhvHly7vRsHK+tQyMSaeK782RHpY33qxPLc8LmoQLb2EuiQxXj9POYkYBQ74qkrZnvKVlR3WoyQWeDOXnSY2wbNFfkP8ET4ElwyuIIEriwYhab0OIrnnrO8X82/SPZxHwEd3aQjQ6uhiw8paDspJbS5WjEfuwY16KVVUYlhbtAwGjvc6aK0NBm+LH9fMLpAE6gfGZNy0gzMDorVNbkQK1IoAGD8p9ZHdB0F3FwkILEjUiQW6nK+/fKDNJ0TBbpgZUpY8bR460qzxKdeZ1yPDqX2Cjh6fkCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAYL4iD6noMJAt63kDED4RB2mII/lssvHhcxuDpOm3Ims9urubFWEpvV5TgIBAxy9PBinOdjhO1kGJJnYi7F1jv1qnZwTV1JhYbvxv3+vk0jaiu7Ew7G3ASlzruXyMhN6t6jk9MpaWGl5Uw1T+gNRUcWQRR44g3ahQRIS/UHkaV+vcpOa8j186/1X0ULHfbcVQk4LMmJeXqNs8sBAUdKU/c6ssvj8jfJ4SfrurcBhY5UBTOdQOXTPY85aU3iFloerx7Oi9EHewxInOrU5XzqqTz2AQPXezexVeAQxP27lzqCmYC7CFiam6QBr06VebkmnPLfs76n8CDc1cwE6gUl0rMA==',
        'x-ibm-client-id': 'b74b3ed4-1314-4132-9024-83e740b11c39',
        'x-request-id': '95126d8f-ae9d-4ac3-ac9e-c357dcd78811'
    }
    return get_request_with_tls(request, resource)


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
    base_url = 'https://api-sandbox.rabobank.nl/openapi/sandbox/' if request.mode == 'SANDBOX' \
        else 'https://api.rabobank.nl/openapi/'

    response = requests.get(url=base_url + resource,
                            params=request.args.to_dict(),
                            headers=request.headers,
                            cert=('cert.pem', 'key.pem'))
    return {'payload': response.text, 'status': response.status_code}
