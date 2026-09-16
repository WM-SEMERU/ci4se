def set_sparsemem(self, sparsemem):
    if sparsemem:
        flag = 1
    else:
        flag = 0
    yield from self._hypervisor.send('vm set_sparse_mem "{name}" {sparsemem}'
        .format(name=self._name, sparsemem=flag))
    if sparsemem:
        log.info('Router "{name}" [{id}]: sparse memory enabled'.format(
            name=self._name, id=self._id))
    else:
        log.info('Router "{name}" [{id}]: sparse memory disabled'.format(
            name=self._name, id=self._id))
    self._sparsemem = sparsemem