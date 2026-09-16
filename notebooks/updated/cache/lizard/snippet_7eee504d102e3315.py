def rpc_connect(self):
    if self.coin in COINS:
        rpc_url = COINS[self.coin]['rpc-url'] + ':'
        if self.testnet:
            rpc_url += COINS[self.coin]['rpc-port-testnet']
        else:
            rpc_url += COINS[self.coin]['rpc-port']
        self.rpc = pyjsonrpc.HttpClient(url=rpc_url, username=COINS[self.
            coin]['rpc-user'], password=COINS[self.coin]['rpc-password'])
        self.logger.debug(self.coin, 'RPC connection ok')
        self.connected = True
    else:
        self.logger.debug(self.coin, 'bridge not found')
    return self.connected