from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

def generate_keys():
    private_key = dsa.generate_private_key(key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def generate_signature(message,private_key):
    signature = private_key.sign(message, hashes.SHA256())
    return signature

def verify_signature(message, public_key, signature):
    try:
        public_key.verify(message, signature, hashes.SHA256())
        print ("valid sign")
    
    except InvalidSignature:
        print("invalid sign")


message = b"Secure message"
private_key, publickey = generate_keys()
signature = generate_signature(message, private_key)
print(signature)