class Login:

    lista = []

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def createAccount(self):
        account = {"username": self.user, "password": self.password }
        # userPRINT = account.get("user")
        # passwordPRINT = account.get("password")
        Login.lista.append(account)
        return account #userPRINT, passwordPRINT
