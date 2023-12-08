class Address:
    def __init__(self, country: str, state: str, city: str,
                 street_address: str, post_code: str, user_id: str) -> None:
        self.country: str = country
        self.state: str = state
        self.city: str = city
        self.street_address: str = street_address
        self.post_code: str = post_code
        self.user_id: str = None
