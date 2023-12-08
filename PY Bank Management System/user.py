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

        if isinstance(address, Address):
            self.addresses.append(address)
            address.user_id = self.id
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise Exception("Invalid address...")
                else:
                    self.addresses.append(entry)
                    entry.user_id = self.id

    def generate_id(self) -> str:
        # TODO: Write algorithm to generate an ID.
        return "1234"
