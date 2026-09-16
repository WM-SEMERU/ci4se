def signatures(self, transaction):
    if not self.multi_wallet:
        raise DecryptionError(
            'This wallet must be unlocked with wallet.unlock(passphrase)')
    return self.multi_wallet.signatures(transaction)