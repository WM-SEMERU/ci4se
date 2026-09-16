def nic_list(self, bridge):
    args = {'name': bridge}
    self._bridge_chk.check(args)
    return self._client.json('bridge.nic-list', args)