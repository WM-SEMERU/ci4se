def read_with_mac(self, *blocks):
    log.debug('read {0} block(s) with mac'.format(len(blocks)))
    if self._sk is None or self._iv is None:
        raise RuntimeError('authentication required')
    service_list = [tt3.ServiceCode(0, 11)]
    block_list = [tt3.BlockCode(n) for n in blocks]
    block_list.append(tt3.BlockCode(129))
    data = self.read_without_encryption(service_list, block_list)
    data, mac = data[0:-16], data[-16:-8]
    if mac != self.generate_mac(data, self._sk, self._iv):
        log.warning('mac verification failed')
    else:
        return data