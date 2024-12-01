# Function to calculate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    d = 1
    while (e * d) % phi != 1:
        d += 1
    return d

# RSA Key generation
def rsa_keygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that 1 < e < phi(n) and gcd(e, phi) = 1
    e = 2
    while gcd(e, phi) != 1:
        e += 1

    # Compute d such that (e * d) % phi = 1
    d = mod_inverse(e, phi)

    # Public and private keys
    return (e, n), (d, n)

# RSA Encryption
def rsa_encrypt(plaintext, pub_key):
    e, n = pub_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# RSA Decryption
def rsa_decrypt(ciphertext, priv_key):
    d, n = priv_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# Example usage
p = 61  # Example prime number
q = 53  # Example prime number

# Generate public and private keys
public_key, private_key = rsa_keygen(p, q)

# Original message
message = "HELLO"

# Encrypt the message
encrypted_message = rsa_encrypt(message, public_key)
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message
decrypted_message = rsa_decrypt(encrypted_message, private_key)
print(f"Decrypted Message: {decrypted_message}")
