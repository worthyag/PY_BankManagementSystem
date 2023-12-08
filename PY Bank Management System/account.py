class Account:
    def __init__(self, id: str) -> None:
        self.user_id: str = id
        self.account_number: str = self.generate_account_number()
        self.balance: float = 0.0

    def generate_account_number(self) -> str:
        pass

    def view_balance(self) -> None:
        pass

    def deposit_money(self) -> None:
        pass

    def withdraw_money(self) -> None:
        pass

    def transfer_money(self) -> None:
        pass

    def view_account_info(self) -> None:
        pass

    def update_account_info(self) -> None:
        pass


def test():
    from user import User
    import datetime
    from address import Address

    address = Address("UK", "England", "London", "24 church road", "N7 4HJ")
    address2 = Address("France", "n/a", "Paris",
                       "32 l'eglise cors", "GE 573BS")

    user = User("Jane", "Doe", "jdoe@email.com",
                datetime.date.today(), [address, address2])

    print(user.addresses[0].country)
    print(user.addresses[1].country)
    print("-----------------------------------")
    print(user.addresses[0].state)
    print(user.addresses[1].state)
    print("-----------------------------------")
    print(user.addresses[0].city)
    print(user.addresses[1].city)
    print("-----------------------------------")
    print(user.addresses[0].street_address)
    print(user.addresses[1].street_address)
    print("-----------------------------------")
    print(user.addresses[0].post_code)
    print(user.addresses[1].post_code)
    print("-----------------------------------")
    print(user.addresses[0].user_id)
    print(user.addresses[1].user_id)
    print("-----------------------------------")

    address3 = Address("Canada", "n/a", "Montreal",
                       "77 horse pickens", "XCV 67K")

    user.add_address(address3)
    print(user.addresses[2].user_id)
    print(user.addresses[2].street_address)
    print(user.addresses[2].city)
    print(user.addresses[2].post_code)
    print(user.addresses[2].state)
    print(user.addresses[2].country)

    # user.add_address("address3")  # Exception works


# test()
