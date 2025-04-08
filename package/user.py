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

# c = ''
# while c != 'N':
#     user = input("User: ")
#     password = input("Password: ")

#     pessoa = Login(user, password)
#     c = input(": ")


# user = input("User: ")
# password = input("Password: ")

# pessoa = Login(user, password)

# print(pessoa.createAccount())
# userPRINT, passwordPRINT = pessoa.createAccount()

# print("\n","Usuário:", userPRINT)
# print(" Senha:", passwordPRINT)

# account = pessoa.createAccount()

# user = account.get("user")
# password = account.get("password")

# print(f"Usuario: {user}")
# print(f"Senha: {password}")