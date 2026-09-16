def verify_message(address, message, signature):
    bitcoin_message = BitcoinMessage(message)
    verified = VerifyMessage(address, bitcoin_message, signature)
    return verified