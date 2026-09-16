def generate_queue_shared_access_signature(self, queue_name, permission=
    None, expiry=None, start=None, id=None, ip=None, protocol=None):
    _validate_not_none('queue_name', queue_name)
    _validate_not_none('self.account_name', self.account_name)
    _validate_not_none('self.account_key', self.account_key)
    sas = QueueSharedAccessSignature(self.account_name, self.account_key)
    return sas.generate_queue(queue_name, permission=permission, expiry=
        expiry, start=start, id=id, ip=ip, protocol=protocol)