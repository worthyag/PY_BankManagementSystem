from name import Name
from address import Address
import datetime


class User(Name):
    def __init__(self, first_name: str, last_name: str, email: str,
                 dob: datetime.date, address) -> None:
        super().__init__(first_name, last_name)

        self.id = self.generate_id()
        self.email = email
        self.date_of_birth = dob
        self.addresses: list = []
        self.username: str
        self.password: str

        # if isinstance(address, Address):
        #     self.addresses.append(address)
        #     address.
    def generate_id(self) -> str:
        pass
