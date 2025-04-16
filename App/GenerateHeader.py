import hashlib
import hmac
import time
import uuid
import base64
import os 
import json

def generate_header():
    credentials_file = os.path.join(os.path.dirname(__file__),"../../Secrets/credentials.json")

    # Read the credentials from the file
    with open(credentials_file, "r") as file:
        credentials = json.load(file)
        

    token = credentials["token"]
    secret = credentials["secret"]

    # print("token:", token)
    # print("secret:", secret)

    nonce = str(uuid.uuid4())
    t = int(round(time.time() * 1000))
    string_to_sign = "{}{}{}".format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, "utf-8")
    secret = bytes(secret, "utf-8")
    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest()
    )

    apiHeader = {}
    apiHeader["Authorization"] = token
    apiHeader["Content-Type"] = "application/json"
    apiHeader["charset"] = "utf8"
    apiHeader["t"] = str(t)
    apiHeader["sign"] = str(sign, "utf-8")
    apiHeader["nonce"] = nonce

    return apiHeader

# print(generate_header())