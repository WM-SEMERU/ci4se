def setTxPower(self, tx_power, peername=None):
    if peername:
        protocols = [p for p in self.protocols if p.peername[0] == peername]
    else:
        protocols = self.protocols
    for proto in protocols:
        proto.setTxPower(tx_power)