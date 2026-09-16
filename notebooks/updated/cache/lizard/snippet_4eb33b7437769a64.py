def getinfo(self):
    try:
        old_getinfo = AuthServiceProxy(self.__service_url, 'getinfo', self.
            __timeout, self.__conn, True)
        res = old_getinfo()
        if 'error' not in res:
            return res
    except JSONRPCException:
        pass
    network_info = self.getnetworkinfo()
    blockchain_info = self.getblockchaininfo()
    try:
        wallet_info = self.getwalletinfo()
    except:
        wallet_info = {'walletversion': None, 'balance': None,
            'keypoololdest': None, 'keypoolsize': None, 'paytxfee': None}
    res = {'version': network_info['version'], 'protocolversion':
        network_info['protocolversion'], 'walletversion': wallet_info[
        'walletversion'], 'balance': wallet_info['balance'], 'blocks':
        blockchain_info['blocks'], 'timeoffset': network_info['timeoffset'],
        'connections': network_info['connections'], 'proxy': network_info[
        'networks'], 'difficulty': blockchain_info['difficulty'], 'testnet':
        blockchain_info['chain'] == 'testnet', 'keypoololdest': wallet_info
        ['keypoololdest'], 'keypoolsize': wallet_info['keypoolsize'],
        'paytxfee': wallet_info['paytxfee'], 'errors': network_info['warnings']
        }
    for k in ['unlocked_until', 'relayfee', 'paytxfee']:
        if wallet_info.has_key(k):
            res[k] = wallet_info[k]
    return res