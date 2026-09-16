def Create(path, password, generate_default_key=True):
    wallet = UserWallet(path=path, passwordKey=password, create=True)
    if generate_default_key:
        wallet.CreateKey()
    return wallet