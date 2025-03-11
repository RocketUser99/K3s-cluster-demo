# ------------------------------------------------------------
# Name: Tou Yang
# GitHub Link: https://github.com/RocketUser99
# This script generates a custom Kubernetes token using a combination of access and secret keys.
# ------------------------------------------------------------

import time
import hashlib
import base64
import json

# Generate a token for kubernetes
def generate_token(secret_key, access_key, expiration_time=3600):
    # Get the current timestamp and the expiration time.
    current_time = int(time.time())
    expiration = current_time + expiration_time
    
    # Create a string to be hashed
    token_string = f"{access_key}:{expiration}"
    
    # Hash the string using SHA-256 
    hash_object = hashlib.sha256(token_string.encode('utf-8') + secret_key.encode('utf-8'))
    signature = base64.b64encode(hash_object.digest()).decode('utf-8')

    # Create a final token.
    token = {
        "access_key": access_key,
        "expiration": expiration,
        "signature": signature,
        "token": f"{access_key}:{expiration}:{signature}"
    }
    
    return token

# Please change both keys below
secret_key = "ks3_super_secret_key"
access_key = "ks3-demo-token"

token = generate_token(secret_key, access_key)
print("Generated Token: " + token["token"])
