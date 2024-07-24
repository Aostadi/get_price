import register

menu = "1.register \n2.exit \nplease select one(only number): "
chioce = input(menu)
if chioce=="1":
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    register.register(name=name, email=email)
else:
    exit()
    