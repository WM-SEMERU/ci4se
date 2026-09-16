def _check_file(self, filename):
    log_threshold = Nit.SEVERITY.get(self._severity, Nit.COMMENT)
    failure_count = 0
    fail_threshold = Nit.WARNING if self._strict else Nit.ERROR
    for i, nit in enumerate(self._get_nits(filename)):
        if i == 0:
            print()
        if nit.severity >= log_threshold:
            print('{nit}\n'.format(nit=nit))
        if nit.severity >= fail_threshold:
            failure_count += 1
    return failure_count