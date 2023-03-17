class User:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.full_name = None
        self.number = None
        self.email_address = None

    def __str__(self):
        return f"{self.first_name}"
