class Address:
    def __init__(self, country: str, state: str, city: str,
                 street_address: str, post_code: str) -> None:
        self.country: str = country
        self.state: str = state
        self.city: str = city
        self.street_address: str = street_address
        self._post_code: str = post_code
        self.user_id: str = None


address = Address("country", "state", "city", "street address", "post code")

print(address)

print(address.country)
print(address.state)
print(address.city)
print(address.street_address)
print(address._post_code)
print(address.user_id)
