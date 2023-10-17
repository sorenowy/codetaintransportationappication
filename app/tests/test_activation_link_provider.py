import hashlib
from fastapi import Request
from random import randbytes

from app.security.activation_link_provider import decrypt_verification_code_from_token


def test_decrypt_verification_code_from_token_is_equal():
    token = "122166dd9e2d617246da9af9d7d3cd6f"
    hashedCode = hashlib.sha256()
    hashedCode.update(bytes.fromhex(token))
    verification_code = hashedCode.hexdigest()
    
    assert verification_code == decrypt_verification_code_from_token(token)