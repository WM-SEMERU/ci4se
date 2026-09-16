def __init_config_params(self, config):
    if self.version >= (2, 4):
        params = config.get('setParameter', {})
        params.setdefault('enableTestCommands', 1)
        if self.version >= (4, 1) and not self.is_mongos:
            params.setdefault('transactionLifetimeLimitSeconds', 3)
        if self.version >= (4, 0) and not self.is_mongos:
            params.setdefault('maxTransactionLockRequestTimeoutMillis', 25)
        config['setParameter'] = params
    compressors = config.get('networkMessageCompressors')
    if compressors is None:
        if self.version >= (4, 1, 7):
            config['networkMessageCompressors'] = 'zstd,zlib,snappy,noop'
        elif self.version >= (3, 5, 9):
            config['networkMessageCompressors'] = 'zlib,snappy,noop'
        elif self.version >= (3, 4):
            config['networkMessageCompressors'] = 'snappy,noop'