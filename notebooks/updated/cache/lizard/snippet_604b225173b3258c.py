def getExpirations(self, contract_identifier, expired=0):
    expirations = []
    contracts = self.contractDetails(contract_identifier)['contracts']
    if contracts[0].m_secType not in ('FUT', 'FOP', 'OPT'):
        return []
    for contract in contracts:
        expirations.append(contract.m_expiry)
    expirations = list(map(int, expirations))
    today = int(datetime.now().strftime('%Y%m%d'))
    closest = min(expirations, key=lambda x: abs(x - today))
    expirations = expirations[expirations.index(closest) - expired:]
    return tuple(expirations)