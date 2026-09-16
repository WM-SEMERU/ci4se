def info(self, uuid):
    args = {'uuid': uuid}
    self._domain_action_chk.check(args)
    return self._client.json('kvm.info', args)