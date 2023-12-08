class Display:
    def __init__(self) -> None:
        pass

    def welcome_message(self) -> None:
        print("Welcome to Worthy Bank.")

    def display_menu(self) -> None:
        print("Worthy Bank" /
              "==============" /
              "1. Login")

    def start_bank(self) -> None:
        self.welcome_message()
        self.display_menu()
