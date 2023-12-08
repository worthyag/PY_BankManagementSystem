import name


class User(name.Name):
    def __init__(self, first_name: str, last_name: str) -> None:
        super().__init__(first_name, last_name)
