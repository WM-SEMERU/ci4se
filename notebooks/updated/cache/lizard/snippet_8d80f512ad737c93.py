def HandlePeerInfoReceived(self, payload):
    addrs = IOHelper.AsSerializableWithType(payload,
        'neo.Network.Payloads.AddrPayload.AddrPayload')
    if not addrs:
        return
    for nawt in addrs.NetworkAddressesWithTime:
        self.leader.RemoteNodePeerReceived(nawt.Address, nawt.Port, self.prefix
            )