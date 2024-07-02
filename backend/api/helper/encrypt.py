from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import os
import base64

def generate_key():
  salt = os.urandom(16)
  kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=salt,
      iterations=480000,
  )
  key = base64.urlsafe_b64encode(kdf.derive(b'password'))
  return key

def encrypt(password):
  f = Fernet(b'6eB5eYRnCPABkGh5uac1LojrOTW8aZhbmFahCSkrNzk=')

  token = f.encrypt(password.encode('ascii'))
  return token.decode('ascii')

def decrypt(hashed_password):
  f = Fernet(b'6eB5eYRnCPABkGh5uac1LojrOTW8aZhbmFahCSkrNzk=')

  password = f.decrypt(hashed_password)
  print(password.decode('ascii'))
  return password.decode('ascii')

# simulando encriptografia
# print(generate_key())
# print(encrypt('vini400'))
# decrypt()
