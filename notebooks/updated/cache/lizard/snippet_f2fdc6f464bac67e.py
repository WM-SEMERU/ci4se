def dump_partition(self, parameters, wait_for_completion=True,
    operation_timeout=None):
    result = self.manager.session.post(self.uri + '/operations/scsi-dump',
        wait_for_completion=wait_for_completion, operation_timeout=
        operation_timeout, body=parameters)
    return result