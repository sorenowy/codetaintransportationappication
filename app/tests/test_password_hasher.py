import hashlib

from app.security.password_hasher import hash_password, read_hashed_password
from app.config.constants import PASSWORD_SALT


def test_hash_password_is_equal():
    password = "TestPassword123!"
    hashed_password = hashlib.sha512(password.encode('utf-8') + PASSWORD_SALT.encode('utf-8')).hexdigest() # logic behind hash password
    assert hash_password(password) == hashed_password
    
def test_read_hashed_password_is_valid():
    password = "TestPassword12354!"
    hashed_password = hash_password(password)
    assert read_hashed_password(password, hashed_password) is True