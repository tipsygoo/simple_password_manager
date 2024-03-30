import base64, os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

from cryptography.fernet import Fernet

SALT = os.urandom(16)

def derive_key_from_password(password: str, salt: bytes = SALT, length: int = 32) -> any:
    """_summary_

    Args:
        password (str): _description_
        salt (bytes, optional): _description_. Defaults to SALT.
        length (int, optional): _description_. Defaults to 32.

    Returns:
        any: _description_
    """
    kdf = kdf.pbkdf2.PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def generate_fernet_key(master_password: str) -> bytes:
    """_summary_

    Args:
        master_password (str): _description_

    Returns:
        bytes: _description_
    """
    key = derive_key_from_password(master_password, length=32)
    return base64.urlsafe_b64encode(key)

def encrypt_password(password: str, master_password: str) -> str:
    """_summary_

    Args:
        password (str): _description_
        master_password (str): _description_

    Returns:
        str: _description_
    """
    key = generate_fernet_key(master_password)
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password: str, master_password: str) -> str:
    """_summary_

    Args:
        encrypted_password (str): _description_
        master_password (str): _description_

    Returns:
        str: _description_
    """
    key = generate_fernet_key(master_password)
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_password.encode()).decode()
