from dataclasses import dataclass


@dataclass
class Token:
    email: str
    user_id: int
    is_admin: bool
    is_verified: bool