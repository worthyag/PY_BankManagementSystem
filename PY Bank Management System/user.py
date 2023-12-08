from name import Name
from address import Address
import datetime


class User(Name):
    def __init__(self, first_name: str, last_name: str, id: str, email: str,
                 dob: datetime.date) -> None:
        super().__init__(first_name, last_name)

        self.id = id
        self.email = email
        self.date_of_birth = dob
        self.address: object
        self.username: str
        self.password: str
