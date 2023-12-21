class Display:
    def __init__(self) -> None:
        pass

    def welcome_message(self) -> None:
        print("Welcome to Worthy Bank.")

    def display_menu(self) -> None:
        print("\n   Menu \
              \n============ \
              \n1. Login \
              \n2. Create an account")

    def start_bank(self) -> None:
        self.welcome_message()
        self.display_menu()


# Check whether False is returned from create account, if so, give
# user the chance to start again, or to pick another option.
