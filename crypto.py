from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os


def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Function to encrypt a message


def encrypt_message(message: str, password: str) -> str:
    salt = os.urandom(16)
    key = generate_key(password, salt)
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return base64.urlsafe_b64encode(salt + encrypted_message).decode()

# Function to decrypt a message


def decrypt_message(encrypted_message: str, password: str) -> str:
    decoded_message = base64.urlsafe_b64decode(encrypted_message)
    salt, encrypted_message = decoded_message[:16], decoded_message[16:]
    key = generate_key(password, salt)
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()
