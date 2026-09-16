def balance(self, account: Address):
    return self.web3.eth.getBalance(to_checksum_address(account), 'pending')