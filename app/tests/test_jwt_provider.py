import jwt
from app.security.jwt_provider import signJWT, decodeJWT
from app.config.constants import SECRET_KEY, JWT_ALGORITHM
from app.model.user import UserResponseDTO
from app.model.token import Token


def test_signJWT_is_correct():
    user = UserResponseDTO(**{
        'email': "jan@nowak.pl",
        'id': 123,
        'name': 'Jan',
        'surname': 'Kowalski',
        'address': 'Kowalska 32, 64-312',
        "is_admin": True,
        "is_verified": False
    })
    payload = {
        "email": user.email,
        "user_id": user.id,
        "is_admin": user.is_admin,
        "is_verified": user.is_verified
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
    
    assert token == signJWT(user)
    
def test_decodeJWT_is_correct():
    user = UserResponseDTO(**{
        'email': "jan@nowak.pl",
        'id': 123,
        'name': 'Jan',
        'surname': 'Kowalski',
        'address': 'Kowalska 32, 64-312',
        "is_admin": True,
        "is_verified": False
    })
    payload = {
        "email": user.email,
        "user_id": user.id,
        "is_admin": user.is_admin,
        "is_verified": user.is_verified
    }
    token_to_verify = Token(**{
        "email": user.email,
        "user_id": user.id,
        "is_admin": user.is_admin,
        "is_verified": user.is_verified
    })
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
    decoded_token = decodeJWT(token)
    
    assert token_to_verify == decoded_token