class Account:
    def __init__(self, id) -> None:
        self.user_id = id
        self.account_number = self.generateAccountNumber()
        self.balance = 0

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
