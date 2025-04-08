from package.user import Login

user = input("User: ")
password = input("Password: ")

pessoa = Login(user, password)
account = pessoa.createAccount()

user = account.get("username")
password = account.get("password")

print(f"Usuario: {user}")
print(f"Senha: {password}")