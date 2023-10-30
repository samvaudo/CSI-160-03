# Reviewing functions, param, placeholders & saving data

def acct_info():
    name = input("User name:")
    pswd = input("Password:")
    acct = input("Accout number:")
    print("thanks for the data!")
    storeData(name, pswd, acct)


def storeData(name, pswd, acct):
    print("Username is", name)
    print("Password is", pswd)
    print("Account number is", acct)


acct_info()
