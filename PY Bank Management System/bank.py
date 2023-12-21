from account import Account
from user import User
from account import Account
from datetime import date


class HelperFunctions:
    def __init__(self) -> None:
        pass

    def generate_birthday(self):
        error_char = ""

        for i in range(3):
            try:
                error_char += "Y"
                year = int(input("Enter your year of birth (YYYY) > "))
                if year > int(date.today().year) or year < 1900:
                    raise Exception

                error_char += "M"
                month = int(input("Enter your month of birth (MM) > "))
                if month > 12 or month < 1:
                    raise Exception

                error_char += "D"
                day = int(input("Enter your day of birth (DD) > "))
                if day > 31 or day < 1:
                    raise Exception

                # Checks any error that was missed (such as setting the
                # birthday to 30th February)
                birth_date = date(year, month, day)
                return birth_date

            except:
                if error_char == "Y":
                    print("Invalid birth year.")
                if error_char == "YM":
                    print("Invalid birth month.")
                if error_char == "YMD":
                    print("Invalid birth date.")

                if i == 2:
                    print("You've reached your registry limit.")

    def get_user_info(self):
        # Add input validation.
        first_name = input("Please enter your first name > ")
        last_name = input("Please enter your last name > ")
        email = input("Please your email > ")

        return (first_name, last_name, email)


class Bank:
    helper = HelperFunctions()

    def __init__(self) -> None:
        number_of_accounts: int = 0

    def authenticate_account(self) -> None:
        pass

    def create_account(self) -> None:
        # TODO: Check that the generated ID is unique.
        # To create an account, a user must be generated and an account
        # to go with them.
        first_name, last_name, email = self.helper.get_user_info()
        birth_date = self.helper.generate_birthday()

        print(first_name, last_name, email)
        print(f"dob: {birth_date}")

        # Get user to check and validate info at the end
        # User input validation (check whether the name is long enough,
        # or only contains letters)
        # Check the age of the user, whether they are a minor or not.
        # newUser = User()

    def close_account(self) -> None:
        pass


if __name__ == "__main__":
    bank = Bank()
    bank.create_account()

    # helper = HelperFunctions()
    # print(helper.generate_birthday())

    # print(date(2023, 2, 28))
