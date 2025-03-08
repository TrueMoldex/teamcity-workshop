from attr import dataclass


@dataclass
class User:
    user: str
    password: str