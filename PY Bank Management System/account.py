class Account:
    def __init__(self, id: str) -> None:
        self.user_id: str = id
        self.account_number: str = self.generate_account_number()
        self.balance: float = 0

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
