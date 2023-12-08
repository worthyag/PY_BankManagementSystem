class Account:
    def __init__(self, id: str) -> None:
        self.user_id: str = id
        self.account_number: str = self.generateAccountNumber()
        self.balance: float = 0

    def generateAccountNumber(self) -> str:
        pass

    def viewBalance(self) -> None:
        pass

    def depositMoney(self) -> None:
        pass

    def withdrawMoney(self) -> None:
        pass

    def transferMoney(self) -> None:
        pass

    def viewAccountInfo(self) -> None:
        pass

    def updateAccountInfo(self) -> None:
        pass
