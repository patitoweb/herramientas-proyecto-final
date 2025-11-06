import hashlib

texto = "hola"
hash_hex = hashlib.sha256(texto.encode()).hexdigest()
print("SHA-256:", hash_hex)
