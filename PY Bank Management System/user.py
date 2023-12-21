from name import Name
from address import Address
from datetime import datetime
import random
import re

# TODO: Need to comment my code.


class User(Name):
    def __init__(self, first_name: str, last_name: str, email: str,
                 dob: datetime, address) -> None:
        super().__init__(first_name, last_name)

        self.id = self.generate_id()
        self.email = email
        self.date_of_birth = dob
        self.addresses: list = []

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
        else:
            raise Exception("Invalid address...")

    def generate_id(self) -> str:
        # Using time and name to generate a unique id.
        # The bank class must ensure that this id is truly unique, though
        #  it is unlikely to not be.
        id = str(datetime.now())
        match = r"[-.:\s]"
        id = f"{self.first_name[0].capitalize()}{self.last_name[0].capitalize()}{
            re.sub(match, "", id)}"
        return id

    def add_address(self, address) -> None:
        if isinstance(address, Address):
            self.addresses.append(address)
            address.user_id = self.id
        else:
            raise Exception("Invalid address...")


if __name__ == "__main__":
    address = Address("UK", "England", "London", "24 church road", "N7 4HJ")
    newUser = User("Worthy", "Albright",
                   "worthy@email.com", datetime(2023, 11, 2),
                   address)

    print(newUser.date_of_birth)
